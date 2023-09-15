# A RESTful API with Basic CRUD Operations

This is a REST API for displaying data from a MongoDB database. It supports dynamic URL parameters, for which the API will query the database and retrieve results. It's endpoints support GET, POST, PATCH and DELETE requests on all database entries.


## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [API Endpoints](#api-endpoints)
  - [Sample Requests and Responses](#sample-requests-and-responses)

## Getting Started

### Prerequisites

- Node.js
- Python 3.6 and above for tests

### Installation

1. Clone the repo
   ```bash
   git clone https://github.com/ndiuel/hng_stage_2.git
   cd hng_stage_2
   ```
2. Install dependencies
   ```bash
   npm install
   pip install requests 
   ```
4. Run the application
   ```bash
   node api/index.js 
   ```
4. Run the tests
   ```bash
   python tests.py
   ```

## Usage

The API is expected to be able to perform CRUD operations on a resource. It also expected to be able to handle dynamic inputs.

### API Endpoints

- Create a Person
- Fetch Persons
- Fetch a Person by ID or Name
- Update a Person by ID or Name
- Delete a Person by ID or Name


### Sample Requests and Responses

#### Create a Person

**Request:**

```http
POST /api/
Content-Type: application/json

{
  "name": "Samuel", "age": 25, "email": ndiuel@gmail.com
}
```

**Reponse:**

```http
{
  "name": "Samuel", "age": 25, "email": ndiuel@gmail.com
}
```

#### Fetch Persons

**Request:**

```http
GET /api/
Content-Type: application/json
```

**Reponse:**

```http
{
  "name": "Samuel", "age": 25, "email": ndiuel@gmail.com
}
```

#### Fetch Persons By Id Or Name

**Request:**

```http
GET /api/Samuel
Content-Type: application/json
```

**Reponse:**

```http
{
  "name": "Samuel", "age": 25, "email": ndiuel@gmail.com
}
```

**Request:**

```http
GET /api/6504db8da541d26b31c8e898
Content-Type: application/json
```

**Reponse:**

```http
{
  "name": "Samuel", "age": 25, "email": ndiuel@gmail.com
}
```

#### Update a Person By Name Or ID

**Request:**

```http
PATCH /api/Samuel
Content-Type: application/json

{
   "age": 15, "email": el@gmail.com
}
```

**Reponse:**

```http
{
  "age": 15, "email": el@gmail.com
}
```

#### Delete a Person By Name Or ID

**Request:**

```http
DELETE /api/Samuel
Content-Type: application/json

**Reponse:**

```http
{
  "message": "Samuel has been deleted"
}
```