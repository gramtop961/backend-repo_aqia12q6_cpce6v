"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Example schemas (retain for reference):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Logic Peak specific schemas

class Lead(BaseModel):
    """
    Leads captured from contact forms or chat widget
    Collection: "lead"
    """
    name: Optional[str] = Field(None, description="Lead name")
    email: Optional[EmailStr] = Field(None, description="Lead email")
    message: str = Field(..., description="Message or inquiry")
    source: str = Field("contact", description="lead source: contact|chat|other")

class ChatMessage(BaseModel):
    """
    Chat messages captured by the assistant widget
    Collection: "chatmessage"
    """
    session_id: str = Field(..., description="Client-side session identifier")
    text: str = Field(..., description="User message text")
    name: Optional[str] = Field(None, description="Optional user name")
    email: Optional[EmailStr] = Field(None, description="Optional user email")
