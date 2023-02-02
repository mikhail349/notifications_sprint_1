run_dev:
	docker compose -f docker-compose.dev.yml up -d
run_prod:
	docker compose up -d --build