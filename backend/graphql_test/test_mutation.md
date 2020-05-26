# Test Mutation

### create mutation

mutation createBlog {
  createBlog(input: {
    title: "How to build GraphQL API with Django.",
    authorId: 1,
    body: "GraphQL is a declarative, strongly typed, data-driven query language to build APIs."
  }) {
    ok
    blog {
      id
      title
      author {
        id
        name
      }
      body
    }
  }
}

### update mutation

mutation updateBlog {
  updateBlog (input: {
    id: 4,
    title: "How to build GraphQL API with Django - 7 steps.",
    authorId: 1,
    body: "GraphQL is a declarative, strongly typed, data-driven query language to build APIs."
  }) {
    ok
    blog {
      id
      title
      author {
        id
        name
      }
      body
    }
  }
}


### delete mutation

mutation deleteBlog {
  deleteBlog (input: {
    id: 4
  }) {
    ok
  }
}

