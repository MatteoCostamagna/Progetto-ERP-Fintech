FROM golang:1.21

RUN apt-get update && apt-get install -y cron

WORKDIR /app

COPY go.mod ./

RUN go mod download

COPY . .

RUN CGO_ENABLED=0 GOOS=linux go build -o /app/bin/etl cmd/main.go

# Add your crontab file
COPY ./crontab /etc/cron.d/cron-job

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/cron-job

# Apply cron job
RUN crontab /etc/cron.d/cron-job

CMD ["cron", "-f"]