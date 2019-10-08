# Discord Ranter Bot
Share rants from [devRant](https://devrant.com/) on your discord server with friends!

## Requirements
- [Docker](https://docs.docker.com/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## How to use
1. Clone this repository
1. Create a bot on your [Discord Developer Portal](https://discordapp.com/developers/applications/) account
1. Copy the tooken from the bot you created
1. Rename `.env.example` to `.env`, edit it and set the `TOOKEN` field to the tooken that you copied previously
1. Run the container with `docker-compose up -d`
1. Invite the bot to your discord server and enjoy 👍