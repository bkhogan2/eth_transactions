.PHONY: load_csv

load_csv:
	docker exec -it eth_transactions-web-1 python manage.py load_csv

.PHONY: super_user

super_user:
	docker exec -it eth_transactions-web-1 python manage.py createsuperuser