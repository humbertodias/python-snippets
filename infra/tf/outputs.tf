output "xp_queue_url" {
  value = aws_sqs_queue.xp_queue.id
}

output "xp_dlq_url" {
  value = aws_sqs_queue.xp_dlq.id
}