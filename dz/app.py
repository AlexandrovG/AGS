from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

API_KEY = "03f26f207494211a9d3cdfcf"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}"

def get_exchange_rate(base_currency, target_currency):
    try:
        url = f"{BASE_URL}/pair/{base_currency}/{target_currency}"
        response = requests.get(url, timeout=5)
        data = response.json()
        
        if data['result'] == 'success':
            return {
                'rate': data['conversion_rate'],
                'success': True,
                'timestamp': datetime.now().isoformat()
            }
    except:
        pass
    
    fallback = {
        'USD': {'EUR': 0.92, 'RUB': 92.5, 'GBP': 0.79, 'JPY': 148.3},
        'EUR': {'USD': 1.09, 'RUB': 100.5, 'GBP': 0.86, 'JPY': 161.0},
        'RUB': {'USD': 0.0108, 'EUR': 0.00995, 'GBP': 0.0085, 'JPY': 1.60},
        'GBP': {'USD': 1.27, 'EUR': 1.16, 'RUB': 117.5, 'JPY': 187.5},
    }
    
    if base_currency in fallback and target_currency in fallback[base_currency]:
        return {
            'rate': fallback[base_currency][target_currency],
            'success': True,
            'timestamp': datetime.now().isoformat(),
            'note': 'кэш'
        }
    
    return {'success': False, 'rate': 1.0}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/rates')
def get_all_rates():
    base = request.args.get('base', 'USD')
    
    try:
        url = f"{BASE_URL}/latest/{base}"
        response = requests.get(url, timeout=5)
        data = response.json()
        
        if data['result'] == 'success':
            popular = ['USD', 'EUR', 'GBP', 'JPY', 'RUB', 'CAD', 'AUD', 'CHF']
            rates = {}
            for currency in popular:
                if currency in data['conversion_rates'] and currency != base:
                    rates[currency] = data['conversion_rates'][currency]
            
            return jsonify({
                'success': True,
                'base': base,
                'rates': rates,
                'date': data.get('time_last_update_utc', '')
            })
    except:
        pass
    
    return jsonify({'success': False, 'rates': {}})

@app.route('/api/convert')
def convert():
    from_curr = request.args.get('from', 'USD')
    to_curr = request.args.get('to', 'EUR')
    amount = float(request.args.get('amount', 1))
    
    try:
        url = f"{BASE_URL}/pair/{from_curr}/{to_curr}/{amount}"
        response = requests.get(url, timeout=5)
        data = response.json()
        
        if data['result'] == 'success':
            return jsonify({
                'success': True,
                'from': from_curr,
                'to': to_curr,
                'amount': amount,
                'rate': data['conversion_rate'],
                'result': data['conversion_result']
            })
    except:
        pass
    
    rate_data = get_exchange_rate(from_curr, to_curr)
    if rate_data['success']:
        result = amount * rate_data['rate']
        return jsonify({
            'success': True,
            'from': from_curr,
            'to': to_curr,
            'amount': amount,
            'rate': rate_data['rate'],
            'result': result,
            'note': 'кэш'
        })
    
    return jsonify({'success': False, 'error': 'Ошибка'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)