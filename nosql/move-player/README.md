docker compose up -d --build


curl -X POST "http://localhost:8000/move?player_id=player123&x=10&y=20"



api-1         | INFO:     192.168.117.1:45108 - "POST /move?player_id=player123&x=10&y=20 HTTP/1.1" 200 OK
localstack-1  | 2026-05-04T16:10:44.388  INFO --- [et.reactor-1] localstack.request.aws     : AWS dynamodb.UpdateItem => 200
localstack-1  | 2026-05-04T16:10:44.390  INFO --- [et.reactor-2] localstack.request.aws     : AWS sqs.DeleteMessage => 200
worker-1      | Processed: {'id': 'd1c58cb0-7beb-4437-9b76-3b74b5d6b1a3', 'type': 'MOVE', 'player_id': 'player123', 'x': 10, 'y': 20}
localstack-1  | 2026-05-04T16:10:50.398  INFO --- [et.reactor-2] localstack.request.aws     : AWS sqs.ReceiveMessage => 200