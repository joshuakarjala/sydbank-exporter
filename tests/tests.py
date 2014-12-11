from nose.tools import assert_raises

from sydbank_exporter import export_transactions


transactions = [
    {
        'amount': 100, # 13 digits
        'from_account_number': '79810001046105', # 15 digits
        'to_reg_number': '7981', # 4 digits
        'to_account_number': '1046139', # 10 digits
        'to_text': 'hej med dig', # 35 chars
        'to_user_name': 'Kaj Nielsen', # 32 chars
        'bilagsnr': 'internal reference number', # 35 chars
        'date': '20150101', # 8 digits (optional)
        'currency': 'DKK' # 3 chars (optional)
    },
    {
        'amount': 50, # 13 digits
        'from_account_number': '79810001046105', # 15 digits
        'to_reg_number': '7981', # 4 digits
        'to_account_number': '1046139', # 10 digits
        'to_text': 'hej med dig 2', # 35 chars
        'to_user_name': 'Tonni Jensn', # 32 chars
        'bilagsnr': 'internal reference number', # 35 chars
        'date': '20150101', # 8 digits (optional)
        'currency': 'DKK' # 3 chars (optional)
    }
]


def test():
    export_transactions(transactions, 150, 2, write_to='test.csv')
