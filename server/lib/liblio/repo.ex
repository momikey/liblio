defmodule Liblio.Repo do
  use Ecto.Repo,
    otp_app: :liblio,
    adapter: Ecto.Adapters.Postgres
end
