table "words" {
  schema = schema.main
  column "id" {
    null = false
    type = integer
  }

  column "name" {
    null = true
    type = varchar
  }

  primary_key {
    columns = [column.id]
  }
}

schema "main" {
}
