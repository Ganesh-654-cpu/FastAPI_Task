# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")

# def home():
#     return {"message": "Welcome to the FastAPI application!"}



from fastapi import FastAPI 

app = FastAPI()

#Home route

@app.get("/")
def home():
    return {"message": "Welcome to the MY FastAPI application!"}


#About page

@app.get("/about")
def about():
    return {"message": "This is about page"}

#Users Route 

@app.get("/user")

def user():
    return {
        "user":["ganesh", "suresh", "ramesh", "mahesh"]
    }
    
    
@app.get ("/users/{user_id}")

def get_user(user_id:int):
    return {"user_id": user_id}




    
from fastapi import FastAPI 

app = FastAPI()

@app.get("/users") 
def get_users(rahul: str = None):
    return {"Name":"rahul"}

@app.get("/products")
def get_users(limit: int =10):
    return {"limit": limit}

@app.get("/items")
def get_users(name: str = None, price: int = 0):
    return {"name": name, 
            "price": price
            }
    
    
    
    
     
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/create_user")
def create_user(user:User):
    return {
        "message": "User Created",
        "data": user
    }
    
    
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# class User(BaseModel):
#     name: str
#     age: int 
#     email: str
    
# @app.post("/create_user")
    
# def create_user(user:User):
#     return {
#         "message": "User Created",
#         "data": user
#     }


class Address(BaseModel):
    city: str
    pincode: int
    
class User(BaseModel):
    name: str
    age: int 
    address: Address
    
    
@app.post("/create_user")
def create_user(user:User):
    return user 


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):

    id: int
    title: str
    completed: bool
    
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "TODO Created", "data": todo}

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"message": "TODO not found"}

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {"message": "TODO Updated", "data": updated_todo}
    return {"message": "TODO not found"}


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message":"Data Deleted"}
    return {"message":"Data Not Found"}


from fastapi import FastAPI 
from pydantic import BaseModel


app = FastAPI()

# PUT /users/101?nitify=true
# {
    
#     "name":"Mohit"
#     "age": 25
# }


user = []

class User(BaseModel):
    name:str 
    age:int
    
@app.post("/users")
def create_user(user:User):
    user.append(user)
    return {
        "message":"User Created",
         "data":user
            }

@app.put("/users/{user_id}")
def update_user(user_id:int, updated_user:User, notify:bool = False):
    if user_id < len(get_users()
                     ):
        user[user_id] = updated_user
        return {
            "massage":"User Updated",
            "data": updated_user,
            "notify": notify,
            "data": user  
        }
        
    return {
        "error": "User not found "
        
    }
    
    
from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    password: str
    
class UserResponse(BaseModel):
    name: str
    age: int
    
@app.post("/users", response_model=UserResponse)
def get_user():
    return{
        "name": "Ganesh Mahajan",
        "age": 22,
        "password": "221122"
    }
        

from fastapi import FastAPI, status, HTTPException

app = FastAPI()

@app.post("/create_user",status_code= status.HTTP_201_CREATED)
def create_user():
    return {
        "message": "User Created"
    }
    
    
@app.get("/user")
def get_user():
    return{
        "status": "Success",
        "message": "User fetched successfully",
        "data": {
            "name": "Rahul Mahajan",
            "age": 21
        }
    }
    
    
@app.get("/usrs/{user_id}")
def get_user(user_id:int):
    if user_id !=1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="User not found"
            )
        
    return {
        "id" : 1,
        "name": "Kajal"
    }
    
    
#Execption Handling

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()


class UserNotFoundException(Exception):
    def __init__(self,name:str):
        self.name = name
        
@app.exception_handler(UserNotFoundException)
def user_not_found_handler(request: Request, exc: UserNotFoundException):

    return JSONResponse(
        status_code=404,
        content={
            "status": "error",
            "message": f"User {exc.name} not found"
        }
    )



        
@app.get("/user/{name}")
def get_user(name:str):
    if name != "Dipak":
        raise UserNotFoundException(name)
    return{
        "name":name
    }
        


# @app.get("users/{user_id}")
# def get_user(user_id:int):
#     if user_id != 1:
#         raise HTTPException(
#             status_code= 404,
#             detail="User Not Found"
#         )
        
#     return{
#         "id":1,
#         "name": "Ravi"
#     }



#Dependency Injection

from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()


# =========================
# Authentication Example
# =========================

def verify_token(token: str = Header(None)):

    if token != "mysecrettoken":
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )

    return {
        "user": "Authorized User"
    }


@app.get("/secure-data")
def secure_data(user=Depends(verify_token)):

    return {
        "message": "Secure data accessed",
        "user": user
    }


# =========================
# Common Dependency Example
# =========================

def common_logic():
    return {
        "message": "Common Logic executed"
    }


@app.get("/home")
def home(data=Depends(common_logic)):
    return data


# =========================
# Current User Example
# =========================

def get_current_user():
    return {
        "user": "Mohini"
    }


@app.get("/profile")
def profile(user=Depends(get_current_user)):
    return user


@app.get("/dashboard")
def dashboard(user=Depends(get_current_user)):
    return user 



#Middleware 

from fastapi import FastAPI,Request
import time

app = FastAPI()

@app.middleware("http")
async def log_middleware(request:Request,call_next):
    start_time = time.time()
    
    responce = await call_next(request)
    
    process_time = time.time()-start_time
    
    print(f"path:{request.url.path}  | Time:{process_time}")
    
    return responce

@app.middleware("http")
async def my_middleware (request: Request, call_next):
    print("Requested Received")
    
    response = await call_next(request)
    
    print("Response Sent")
    
    return response



import sqlite3

from fastapi import FastAPI

app = FastAPI()


# =========================
# SQLite Database Connection
# =========================

conn = sqlite3.connect("test.db", check_same_thread=False)

cursor = conn.cursor()


# =========================
# Create Todo Table
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY,
    title TEXT,
    completed TEXT
)
""")

conn.commit()


# =========================
# Home Route
# =========================

@app.get("/")
def home():
    return {
        "message": "SQLite Connected fine"
    }



from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends, HTTPException


app = FastAPI()


# =========================
# Database Configuration
# =========================

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


# =========================
# Database Session
# =========================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()


# =========================
# Todo Model
# =========================

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)


# =========================
# Create Database Tables
# =========================

Base.metadata.create_all(bind=engine)


# =========================
# Database Dependency
# =========================

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# =========================
# Home API
# =========================

@app.get("/")
def home(db: Session = Depends(get_db)):
    return {
        "message": "DB connected fine"
    }
    
    
    
#Database Integration (SQLalchemy)
#create API 

@app.post("/todos")
def create_todo(title:str,db: Session = Depends(get_db)):
    todo = Todo(title=title,completed="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "message":"Todo Created",
        "data":todo
    }
    
    

#Read all data
@app.get("/todos")
def get_todos(db:Session = Depends(get_db)):
    todos = db.query(Todo).all()
    
    return{
        "Total": len(todos),
        "data": todos
    }
    
   
   
   #Read data based on ID
   
@app.get("/todos{todo_id}")
def get_todo(todo_id= int,db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    
    if not todo:
        raise HTTPException(status_code=404, Detail="Todo not Found")
    return todo



#Update data 

@app.put("/todos/{todo_id}")
def update_todo(
    todo_id: int,
    title: str,
    db: Session = Depends(get_db)
):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    todo.title = title

    db.commit()
    db.refresh(todo)

    return {
        "message": "Todo Updated",
        "data": {
            "id": todo.id,
            "title": todo.title,
            "completed": todo.completed
        }
    }
    
    
#Delete API

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int,db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    
    return{
        "message": "TODO Deleted"
    }
    
    
import time
import asyncio

from fastapi import FastAPI

app = FastAPI()


# =========================
# ASYNCHRONOUS API
# =========================

@app.get("/")
async def home():
    await asyncio.sleep(3)

    return {
        "message": "Async API"
    }


# =========================
# ASYNC TASK
# =========================

async def task():
    await asyncio.sleep(3)
    return "Done" 



#JWT AUTHRNTICATION

from fastapi import FastAPI, HTTPException, Depends, Header
from jose import jwt
from datetime import datetime, timedelta

app = FastAPI()

SECRET_KEY = "mysecret"
ALGORITHM = "HS256"


# =========================
# Create JWT Token
# =========================

def create_token(data: dict):

    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=30)

    to_encode.update({
        "exp": expire
    })

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token



from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import datetime, timedelta
from passlib.context import CryptContext

app = FastAPI()


# =====================================================
# JWT CONFIGURATION
# =====================================================

SECRET_KEY = "mysecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# =====================================================
# PASSWORD HASHING SETUP
# =====================================================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# =====================================================
# OAUTH2 SETUP
# =====================================================

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


# =====================================================
# DUMMY USER DATABASE
# =====================================================

fake_user_db = {
    "admin": {
        "username": "admin",
        "hashed_password": pwd_context.hash("1234")
    }
}


# =====================================================
# HASH PASSWORD
# =====================================================

def hash_password(password: str):
    return pwd_context.hash(password)


# =====================================================
# VERIFY PASSWORD
# =====================================================

def verify_password(
    plain_password: str,
    hashed_password: str
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# =====================================================
# CREATE JWT TOKEN
# =====================================================

def create_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire
    })

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


# =====================================================
# LOGIN API - GENERATE TOKEN
# =====================================================

@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):

    # Find user
    user = fake_user_db.get(
        form_data.username
    )

    # Check username and password
    if not user or not verify_password(
        form_data.password,
        user["hashed_password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    # Create token
    access_token = create_token({
        "sub": form_data.username
    })

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# =====================================================
# VERIFY JWT TOKEN
# =====================================================

def verify_token(
    token: str = Depends(oauth2_scheme)
):

    try:

        # Decode token
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        # Get username
        username = payload.get("sub")

        # Username not found
        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return username

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )


# =====================================================
# PROTECTED ROUTE 1
# =====================================================

@app.get("/secure")
def secure_data(
    user: str = Depends(verify_token)
):

    return {
        "message": "Secure Data Accessed",
        "user": user
    }


# =====================================================
# PROTECTED ROUTE 2
# =====================================================

@app.get("/protected")
def protected_route(
    username: str = Depends(verify_token)
):

    return {
        "message": f"Hello {username}, you have access to this protected route!",
        "user": username
    }


# =====================================================
# HOME
# =====================================================

@app.get("/")
def home():

    return {
        "message": "FastAPI JWT Authentication is Working"
    }
    


    
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil

from config import settings


# =====================================================
# Create FastAPI App
# =====================================================

app = FastAPI()


# =====================================================
# CORS Configuration
# =====================================================

origins = settings.origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================================
# Step 1: Ensure uploads folder exists
# =====================================================

UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


# =====================================================
# Step 2: Static File Setup
# =====================================================

app.mount(
    "/files",
    StaticFiles(directory=UPLOAD_DIR),
    name="files"
)


# =====================================================
# Step 3: Upload File API
# =====================================================

@app.post("/upload")
def upload_file(
    file: UploadFile = File(...)
):

    filename = file.filename

    # Check file selected
    if not filename:
        raise HTTPException(
            status_code=400,
            detail="File not selected"
        )

    # Create file path
    file_path = os.path.join(
        UPLOAD_DIR,
        filename
    )

    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    return {
        "message": "File Uploaded Successfully",
        "fileName": filename,
        "file_url": f"http://127.0.0.1:8000/files/{filename}"
    }


# =====================================================
# Step 4: Get File URL API
# =====================================================

@app.get("/files/{filename}")
def get_file(filename: str):

    file_path = os.path.join(
        UPLOAD_DIR,
        filename
    )

    # Check file exists
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    return {
        "file_url": f"http://127.0.0.1:8000/files/{filename}"
    }


# =====================================================
# Home API
# =====================================================

@app.get("/")
def home():

    return {
        "message": "File Upload API Running"
    }   




#CORS Handling - Cors Origan Resource Sharing -- frontend ko kaise backend ke sath connect kar sakate hai

# =====================================================
# CORS Handling
# Cross-Origin Resource Sharing
# Frontend ko Backend ke saath connect karne ke liye
# =====================================================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# Create FastAPI app
app = FastAPI()


# =====================================================
# Allowed Origins
# Frontend URL
# =====================================================

origins = [
    "http://localhost:5173"
]


# =====================================================
# Add CORS Middleware
# =====================================================

app.add_middleware(
    CORSMiddleware,

    # Allow frontend
    allow_origins=origins, 
   
    

    # Allow cookies/authentication
    allow_credentials=True,

    # Allow GET, POST, PUT, DELETE etc.
    allow_methods=["*"],

    # Allow all headers
    allow_headers=["*"],
)


# =====================================================
# Home API
# =====================================================

@app.get("/")
def home():

    return {
        "message": "CORS Enabled API"
    } 
    
    
    
from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()


# ========================================
# HOME API
# ========================================

@app.get("/")
def home():
    return {
        "message": "Hello Ganesh"
    }


# ========================================
# ADD API
# ========================================

@app.get("/add")
def add():
    a = 10
    b = 20

    return {
        "result": a + b
    }


# ========================================
# GET ALL POSTS
# ========================================

@app.get("/posts")
def get_posts():

    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(
            status_code=500,
            detail="Unable to fetch posts"
        )

    return response.json()


# ========================================
# GET SINGLE POST
# ========================================

@app.get("/posts/{post_id}")
def get_post(post_id: int):

    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )

    return response.json()




#WEB CROWLING USING FASTAPI /// PAGE Pagignation

# import requests 
# from bs4 import BeautifulSoup 
# url = "http://example.com"

# response = requests.get(url)

# soup = BeautifulSoup(requests.text,"html.parse")

# print(soup.title.text)




from fastapi import FastAPI, Request
import requests
from bs4 import BeautifulSoup
import time

from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse


# ==========================================
# FastAPI App
# ==========================================

app = FastAPI()


# ==========================================
# Rate Limiter Setup
# ==========================================

limiter = Limiter(key_func=get_remote_address)

app.state.limiter = limiter


# ==========================================
# Cache Storage
# ==========================================

cache_data = []
last_fetch = 0


# ==========================================
# Rate Limit Error Handler
# ==========================================

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={
            "detail": "Too many requests. Please try again later."
        }
    )


# ==========================================
# News API
# ==========================================

@app.get("/news")
def get_news():

    global cache_data, last_fetch

    start = time.time()

    # Check cache
    if time.time() - last_fetch > 60:

        print("Fetching Fresh Data")

        # Correct URL
        url = "https://news.ycombinator.com/"

        try:
            response = requests.get(
                url,
                timeout=10
            )

            response.raise_for_status()

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            cache_data = [
                item.get_text(strip=True)
                for item in soup.find_all(
                    "span",
                    class_="titleline"
                )
            ]

            last_fetch = time.time()

        except requests.RequestException as e:

            return {
                "error": "Unable to fetch news",
                "details": str(e)
            }

    else:

        print("Using Cache Data")

    end = time.time()

    time_taken = round(
        end - start,
        4
    )

    print("Time Taken:", time_taken)

    return {
        "time_taken": time_taken,
        "data": cache_data[:5]
    }


# ==========================================
# Rate Limited API
# ==========================================

@app.get("/data")
@limiter.limit("5/minute")
def get_data(request: Request):

    return {
        "message": "Success"
    }

