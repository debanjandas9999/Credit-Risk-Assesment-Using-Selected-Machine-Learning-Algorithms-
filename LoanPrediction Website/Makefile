DOCKER_IMAGE=docker.io/debanjandas/loanpredictor:latest

.PHONY: docker-build docker-push

docker-build:
	docker build . -t "${DOCKER_IMAGE}"

docker-push: docker-build
	docker push "${DOCKER_IMAGE}"

docker-run:
	docker run -p 8080:8080 "${DOCKER_IMAGE}"
