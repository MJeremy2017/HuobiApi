# HuobiApi
Huobi REST API Package(source https://github.com/MJeremy2017/HuobiApi)

__Note__: This is not an official package. For more info, please resort to official docs

## Installation
```
pip install huobiApi
```

## Get Accounts ID

```
import os
from huobiApi.service import HuobiSVC

ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')

svc = HuobiSVC(ACCESS_KEY, SECRET_KEY)

svc.get_accounts()
```
---
```
{'status': 'ok',
 'data': [{'id': 01, 'type': 'spot', 'subtype': '', 'state': 'working'},
  {'id': 02, 'type': 'margin', 'subtype': 'btcusdt', 'state': 'working'},
  {'id': 03, 'type': 'margin', 'subtype': 'eosusdt', 'state': 'working'},
  {'id': 04, 'type': 'margin', 'subtype': 'ethusdt', 'state': 'working'},
  {'id': 05, 'type': 'margin', 'subtype': 'neousdt', 'state': 'working'},
  {'id': 06, 'type': 'otc', 'subtype': '', 'state': 'working'},
  {'id': 07, 'type': 'super-margin', 'subtype': '', 'state': 'working'}]}

```

## Get Kline Data
```
symbol = 'btcusdt'
res = svc.get_kline(symbol, '60min', size=50)
```
---
```
{'status': 'ok',
 'ch': 'market.btcusdt.kline.60min',
 'ts': 1580378774791,
 'data': [{'amount': 66.60260811521935,
   'open': 9364.89,
   'close': 9366.58,
   'high': 9376.21,
   'id': 1580378400,
   'count': 1080,
   'low': 9364.89,
   'vol': 624201.8357696668},
   ...
```

## Place an Order
```
data = svc.send_order(
                acct_id='01',
                amount='0.001',
                price='7999',
                source='api',
                symbol='btcusdt',
                _type='sell-stop-limit',
                stop_price='8000',
                operator='lte'
                )

```
