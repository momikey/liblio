defmodule LiblioWeb.Router do
  use LiblioWeb, :router

  pipeline :browser do
    plug :accepts, ["html"]
    plug :fetch_session
    plug :fetch_flash
    plug :protect_from_forgery
    plug :put_secure_browser_headers
  end

  pipeline :api do
    plug :accepts, ["json"]
  end

  scope "/", LiblioWeb do
    pipe_through :browser

    get "/", PageController, :index
    # Remove this later, once we're sure everything's working right
    resources "/logins", LoginController
  end

  scope "/api", LiblioWeb do
    pipe_through :api
  
    resources "/users", UserController, except: [:new, :edit]
  end
end
