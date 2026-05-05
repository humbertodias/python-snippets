## QR Code Redemption

API for generating and redeeming QR codes to grant in-game items.

## Start stack

```shell
docker compose up -d --build
```

## Generate QR Code

```shell
curl "http://localhost:8000/qr/generate?item_id=sword"
```

Response
```json
{
  "code": "abc12345",
  "item_id": "sword",
  "qr_base64": "iVBORw0KGgoAAAANSUhEUgAA..."
}
```

## Redeem QR Code

```shell
curl "http://localhost:8000/qr/redeem?code=abc12345&player_id=alice"
```

Response
```json
{
  "message": "Item sword granted to player alice"
}
```

## Web Interface

Open a browser at:

http://localhost:8000/

Use the form to generate a QR code or redeem a code directly.

## Docs

http://localhost:8000/docs