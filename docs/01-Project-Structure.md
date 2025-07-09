# Project Structure

Let's iron out our project structure so we can lay things out properly within this learning repo.

Philosophy: Have fun, learn math, futz around with Python, use common AI frameworks and libraries, create something with real world data at small volumes that we can apply what we're learning to, do a lot of my own work.

## Figma Diagram

Let's lay out our project architecture in a Figma Diagram

### Services (or Service Modules)

Can we create a general purpose service that has modules we can split out later? I suspect it's possible with a bit of encapsulation and care

We can probably check out a neat Framework. We could go with one of the classics like Django or Flask but Pyramid looks nice

Let's just start with the API Collector Module to start and we can add modules later when we need them for processing, display, whatever

- Underlying Server
- API Collector Module

### Data Store

The goal here isn't to spend too much time data management, but we're probably going to need a fragmented store environment.

Let's Leave data store specifics to later as we need 'em. For instance as we start pulling in events from various free APIs we can flesh out a stream, then another store for post processing

- Leave as non-specific Data Layer for now

### Elements

- Docker Container around General Service around Module
- Data Layer
- APIs
- Title
- Background
- Labels

Definitely going to need a five color scheme... let's use "Red, A Japanese Good Luck Color" from [Practical Color Combinations](https://openlibrary.org/books/OL36628056M/Practical_Color_Combinations)

Hinoki - Beige with a red tint - 239 218 200
Matsuba-Iro - Green like pine needles - 86 117 76
Ni-Iro - Red with orange shades - 220 84 40
Oshiroi - White like that seen in face makeup during the Edo period - 250 250 247
Honshu - Genuine vermillion as in vermillion coated lacquer ware - 173 51 35
