# cleaning booking request

**Summary**

Make website for local home cleaning company. Schedule a customer cleaning booking online via Django website application.


**Deliverables**

1. All models and columns should have validation as described in the model spec below.
2. Currently we operate in 10 cities, but plan to expand quickly. We need a way to store the list of cities we operate in and the ability to add to the list. You should create a new table to do this.
3. On the Cleaner Form we need a way to select the cities a cleaner works in. This should be a checkbox list populated by the list of cities we operate in. You may need to need to create a new table to store this data.
4. We need a way for customers to signup and schedule a booking all on one form. To accomplish this you will need to do the following:
5. Create a new root page for the application with a form designed for customers to signup and create a booking.
6. On this form, capture all the data needed to create a customer in the database (first name, last name, phone number).
7. If the customer already exists in the database (use phone number to determine this) use the existing record instead of creating a new one. You should probably add a validation to enforce this.
8. Let the customer select what city they are in from the cities table created earlier.
9. Let the customer specify a date and time when they would like their house cleaned.
10. When the user submits the form, look for cleaners that work in the specified city that do not have any bookings that conflict with the time specified.
11. If you can find an available cleaner, create the booking and display the name of the cleaner assigned to the booking.
12. If you can't find an available cleaner, tell the user that we could not fulfill their request.

**Models**

1. **Customer**

  first_name (required), 
  last_name (required), 
  phone_number (optional)
  
2. **Booking**

  customer (required), 
  cleaner (required), 
  date (required), 
  city (required)
  
3. **Cleaner**

  first_name (required), 
  last_name (required), 
  quality_score (required, must be a number between 0.0 and 5.0), 
  city (required)

4. **Cities**

  name (required)

**Install requirement.txt file for dependent libraries**

Command: pip install -r requirement.txt
