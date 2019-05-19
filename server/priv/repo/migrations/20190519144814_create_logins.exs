defmodule Liblio.Repo.Migrations.CreateLogins do
  use Ecto.Migration

  def change do
    create table(:logins) do
      add :email, :string
      add :password, :string
      add :user_id, references(:users, on_delete: :nothing)

      timestamps()
    end

    create unique_index(:logins, [:email])
    create index(:logins, [:user_id])
  end
end
