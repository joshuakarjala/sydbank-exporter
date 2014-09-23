from nose.tools import assert_raises

from sydbank_exporter import export_transactions


transactions = [
    {
        'amount': 100,
        'from_account_number': '79810001046105',
        'to_reg_number': '7981',
        'to_account_number': '1046139',
        'text': 'hej med dig',
        'to_user_name': 'Kaj Nielsen'
    },
    {
        'amount': 50,
        'from_account_number': '79810001046105',
        'to_reg_number': '7981',
        'to_account_number': '1046139',
        'text': 'hej med dig 2',
        'to_user_name': 'Tonni Jensn'
    }
]


def test():
    export_transactions(transactions, 150, 2, write_to='test.csv')
