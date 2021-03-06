# Liblio - a federated platform to connect creators and their audiences

Liblio is (or will be) a platform for creators to reach fans and supporters. It's intended as a place where creators can post links to their work, receive comments, interact with fans, and support their fellow artists, authors, musicians, and other creative people. For fans, the goal is to create a hub for all those whose work you love, as well as a place to discover new creations. It's not a marketplace, an image board, or anything of that sort. Instead, I want Liblio to compleement these by offering a creator-centric social network.

This project is very much a work in progress at present. Check the roadmap below for what's done and what I'm still working on.

## Installation

(TODO)

## Roadmap

All of these are subject to change, and I'll likely add to them as I go.

### Beta 1

These are the bare minimum tasks that need to be finished before Liblio can be considered beta software.

#### Front end

* Personal timeline
* Notifications
* Profile page
* Profile settings (Barely started)
* Avatars (Mostly complete)
* Tagging
* Explorers (These are mostly done, but need more polish.)
* Admin panel (Working on it)
* Site settings (I need to study what kinds of settings Liblio should have.)
* Full i18n (Swap out `labels` objects for proper vue-i18n support.)

#### Back end

* Site settings (This is actually implementing them on the server side.)
* Remember Me
* Rate limiting for some API endpoints
* Database setup for new installs

#### Other

* Installation documentation
* A full suite of tests (unit, integration, etc.)

### Release 1.0

These items are necessary for me to feel comfortable releasing a 1.0 version of Liblio.

* Full federation through ActivityPub (and possibly other networks)
* Multiple localizations
* Theme support
* Easy installer

## License

Liblio is open source software under the [MIT License](LICENSE).