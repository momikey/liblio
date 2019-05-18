defmodule Liblio.Repo.Migrations.CreateUsers do
  use Ecto.Migration

  def change do
    create table(:users) do
      add :shortname, :string, null: false
      add :longname, :string
      add :description, :string
      add :uri, :string

      timestamps()
    end

  end
end
