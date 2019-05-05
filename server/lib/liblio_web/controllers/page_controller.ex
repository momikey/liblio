defmodule LiblioWeb.PageController do
  use LiblioWeb, :controller

  def index(conn, _params) do
    render(conn, "index.html")
  end
end
