# Test Queries


### 1st query

query {
   
  blogs{
    id
    title
    author {
      id
      name
    }
  }
   
}


### 2nd query

query{
   
  blog(id: 1){
    id
    title
    author {
      id
      name
    }
  }
   
}