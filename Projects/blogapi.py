from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
import sqlite3

app=FastAPI() 
conn=sqlite3.connect("Blogs.db",check_same_thread=False)
cursor=conn.cursor()

# create table 
# conn.execute("""
#              create table if not exists Blogs(
#              id int primary key ,
#              name varchar,
#              age int,
#              text varchar
#              )
#              """)
# blogs = [
#     (1, "Alice", 20, "Learning Python programming."),
#     (2, "Bob", 22, "Introduction to Java development."),
#     (3, "Charlie", 19, "C++ basics and object-oriented programming."),
#     (4, "David", 21, "JavaScript for modern web development."),
#     (5, "Emma", 23, "Data Science with Python and Machine Learning.")
# ]


# cursor.executemany("""
#                    Insert into Blogs(id,name,age,text) values (?,?,?,?)
#                    """,blogs)
# conn.commit()


class Blog(BaseModel) :
  id : int
  name : str=Field(max_length=35,description="name should not be less than 35") 
  age : int=Field(ge=18,description="age restricted age should be > 18")
  text : str=Field(min_length=10,max_length=1000,description="about the blog ")

@app.get("/get-blogs")
def get_blogs():
    cursor.execute("SELECT * FROM Blogs")
    blogs = cursor.fetchall()
    
    return [
       {
          "id" : row[0],
          "name" : row[1],
          "age" :row[2],
          "text" :row[3]
       }
       for row in blogs
    ]

@app.post("/post")
def post_blog(blog: Blog):
    try:
        cursor.execute(
            """
            INSERT INTO Blogs (id, name, age, text)
            VALUES (?, ?, ?, ?)
            """,
            (blog.id, blog.name, blog.age, blog.text)
        )
        conn.commit()

        return {
            "message": "Blog created successfully",
            "blog": blog
        }

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="A blog with this ID already exists."
        )
      

   


