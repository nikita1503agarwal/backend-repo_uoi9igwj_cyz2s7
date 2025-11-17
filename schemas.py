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

from pydantic import BaseModel, Field
from typing import Optional, List

# Example schemas (replace with your own):

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

# Catering app schemas

class MenuItem(BaseModel):
    """
    Catering menu items
    Collection name: "menuitem" (lowercase of class name)
    """
    title: str = Field(..., description="Dish name")
    description: Optional[str] = Field(None, description="Short description of the dish")
    price: float = Field(..., ge=0, description="Price per item")
    category: str = Field(..., description="Category, e.g., Appetizer, Main, Dessert")
    image_url: Optional[str] = Field(None, description="Image URL of the dish")
    is_available: bool = Field(True, description="If the item is available for order")
    tags: List[str] = Field(default_factory=list, description="Dietary tags like vegan, spicy")

class OrderItem(BaseModel):
    item_id: str = Field(..., description="Menu item id as string")
    title: str = Field(..., description="Menu item title snapshot")
    price: float = Field(..., ge=0, description="Unit price at order time")
    quantity: int = Field(..., ge=1, description="Quantity ordered")

class Order(BaseModel):
    """
    Orders collection schema
    Collection name: "order"
    """
    customer_name: str = Field(..., description="Customer full name")
    phone: str = Field(..., description="Contact phone number")
    address: str = Field(..., description="Delivery address")
    notes: Optional[str] = Field(None, description="Additional notes or instructions")
    items: List[OrderItem] = Field(..., description="Ordered items")
    total: float = Field(..., ge=0, description="Order total amount")
    status: str = Field("pending", description="Order status: pending, confirmed, preparing, delivering, completed, canceled")

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
