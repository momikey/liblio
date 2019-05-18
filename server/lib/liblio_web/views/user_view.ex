defmodule LiblioWeb.UserView do
  use LiblioWeb, :view
  alias LiblioWeb.UserView

  def render("index.json", %{users: users}) do
    %{data: render_many(users, UserView, "user.json")}
  end

  def render("show.json", %{user: user}) do
    %{data: render_one(user, UserView, "user.json")}
  end

  def render("user.json", %{user: user}) do
    %{id: user.id,
      shortname: user.shortname,
      longname: user.longname,
      description: user.description,
      uri: user.uri}
  end
end
