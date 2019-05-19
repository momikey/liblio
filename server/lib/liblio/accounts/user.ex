defmodule Liblio.Accounts.User do
  use Ecto.Schema
  import Ecto.Changeset

  schema "users" do
    field :description, :string
    field :longname, :string
    field :shortname, :string
    field :uri, :string

    timestamps()
  end

  @doc false
  def changeset(user, attrs) do
    user
    |> cast(attrs, [:shortname, :longname, :description, :uri])
    |> validate_required([:shortname])
    |> validate_length(:shortname, min: 2)
    |> validate_length(:shortname, max: 64)
  end
end
