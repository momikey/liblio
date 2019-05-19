defmodule Liblio.Accounts.Login do
  use Ecto.Schema
  import Ecto.Changeset

  schema "logins" do
    field :email, :string
    field :password, :string
    field :user_id, :id

    timestamps()
  end

  @doc false
  def changeset(login, attrs) do
    login
    |> cast(attrs, [:email, :password])
    |> validate_required([:email, :password])
    |> unique_constraint(:email)
  end
end
