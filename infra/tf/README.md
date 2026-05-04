## TerraForm

docker compose up -d

brew tap hashicorp/tap
brew install hashicorp/tap/terraform

terraform init

terraform apply -auto-approve

aws --endpoint-url=http://localhost:4566 sqs list-queues


aws --endpoint-url=http://localhost:4566 sqs send-message \
  --queue-url http://localhost:4566/000000000000/xp-queue \
  --message-body '{"player_id":"alice","xp":10}'