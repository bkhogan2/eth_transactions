import csv
from django.core.management.base import BaseCommand, CommandError
from eth_transactions.models import Transaction
from datetime import datetime


class Command(BaseCommand):
    help = "Load ethereum transaction data from a CSV file into the Transaction model"

    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str, help='The file path to the CSV file')
    
    def handle(self, *args, **kwargs):
        filepath = kwargs['filepath']

        try:
            with open(filepath, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    Transaction.objects.create(
                        txhash=row['Txhash'],
                        blockno=int(row['Blockno']),
                        unixtimestamp=int(row['UnixTimestamp']),
                        datetime_utc=datetime.strptime(row['DateTime (UTC)'], '%Y-%m-%d %H:%M:%S'),
                        from_address=row['From'],
                        to_address=row['To'],
                        contractaddress=row.get('ContractAddress', ''),
                        value_in_eth=row['Value_IN(ETH)'] or 0,
                        value_out_eth=row['Value_OUT(ETH)'] or 0,
                        current_value_usd=row['CurrentValue @ $1629.6/Eth'] or 0,
                        fee_eth=row['TxnFee(ETH)'] or 0,
                        txnfee_usd=row['TxnFee(USD)'] or 0,
                        historical_sprice_eth=row['Historical $Price/Eth'] or 0,
                        status=row['Status'],
                        errcode=row.get('ErrCode', ''),
                        method=row['Method']
                    )
            print(f"csv file parsed successfully. Filepath={filepath}")
        except Exception as e:
            raise CommandError(f'An error occurred: {str(e)}')