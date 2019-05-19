defmodule LiblioWeb.LoginController do
  use LiblioWeb, :controller

  alias Liblio.Accounts
  alias Liblio.Accounts.Login

  def index(conn, _params) do
    logins = Accounts.list_logins()
    render(conn, "index.html", logins: logins)
  end

  def new(conn, _params) do
    changeset = Accounts.change_login(%Login{})
    render(conn, "new.html", changeset: changeset)
  end

  def create(conn, %{"login" => login_params}) do
    case Accounts.create_login(login_params) do
      {:ok, login} ->
        conn
        |> put_flash(:info, "Login created successfully.")
        |> redirect(to: Routes.login_path(conn, :show, login))

      {:error, %Ecto.Changeset{} = changeset} ->
        render(conn, "new.html", changeset: changeset)
    end
  end

  def show(conn, %{"id" => id}) do
    login = Accounts.get_login!(id)
    render(conn, "show.html", login: login)
  end

  def edit(conn, %{"id" => id}) do
    login = Accounts.get_login!(id)
    changeset = Accounts.change_login(login)
    render(conn, "edit.html", login: login, changeset: changeset)
  end

  def update(conn, %{"id" => id, "login" => login_params}) do
    login = Accounts.get_login!(id)

    case Accounts.update_login(login, login_params) do
      {:ok, login} ->
        conn
        |> put_flash(:info, "Login updated successfully.")
        |> redirect(to: Routes.login_path(conn, :show, login))

      {:error, %Ecto.Changeset{} = changeset} ->
        render(conn, "edit.html", login: login, changeset: changeset)
    end
  end

  def delete(conn, %{"id" => id}) do
    login = Accounts.get_login!(id)
    {:ok, _login} = Accounts.delete_login(login)

    conn
    |> put_flash(:info, "Login deleted successfully.")
    |> redirect(to: Routes.login_path(conn, :index))
  end
end
