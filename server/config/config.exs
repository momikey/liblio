# This file is responsible for configuring your application
# and its dependencies with the aid of the Mix.Config module.
#
# This configuration file is loaded before any dependency and
# is restricted to this project.

# General application configuration
use Mix.Config

config :liblio,
  ecto_repos: [Liblio.Repo]

# Configures the endpoint
config :liblio, LiblioWeb.Endpoint,
  url: [host: "localhost"],
  secret_key_base: "l1q6MKHNuliE4nKh3r1SjQ9aVgCKAwRoYZzmpU0LRf83GkV2tKAlnOESolLxosiF",
  render_errors: [view: LiblioWeb.ErrorView, accepts: ~w(html json)],
  pubsub: [name: Liblio.PubSub, adapter: Phoenix.PubSub.PG2]

# Configures Elixir's Logger
config :logger, :console,
  format: "$time $metadata[$level] $message\n",
  metadata: [:request_id]

# Use Jason for JSON parsing in Phoenix
config :phoenix, :json_library, Jason

# Import environment specific config. This must remain at the bottom
# of this file so it overrides the configuration defined above.
import_config "#{Mix.env()}.exs"
