# Exercise: Coupons - Data Visualization and Analysis

## Running project

Project is ready to run in Docker in a "production ready" environment.  
Just clone the repo and run:

```bash
docker-compose up --build
```

You'll be able to view the project on your 'localhost'.  
Bear in mind that demo data is seeded on building stage, so DB is populated.

### Running backend manually

Please refer to [Backend instructions](backend/README.md)

### Running frontend manually

Pleas refer to [Frontend instructions](frontend/README.md)

## Goals
Your objective is to create a web application able to show relevant statistics from a set of coupons
data with some interactivity.

## Tech requirements

### Frontend
Develop a frontend app with the JavaScript modern framework you prefer (**Vue**, React,Angular, Svelte…). This frontend should be able to show relevant or interesting like:
* How many coupons each coupon type has?
* Number of coupons with discount, the minimum discount, maximum discount, and average discount for **percent-off** coupons
*  Number of coupons with discount, the minimum discount, maximum discount, and average discount for **dollar-off** coupons
*  Whatever you consider insightful

Also, add some type of interactivity to the app:
* When the app loads, it will show all the retailers in a leftbar.
* If you click on a retailer name from the leftbar, all the statistics regarding that retailer will appear on the right part of the screen
* The last item of the sidebar should be an **“All”** item, which shows data from all retailers without filtering
* The results can appear in a JSON format, or even better, in a chart
The design is not required, but a basic good UX will be appreciated.

### Backend
Also, the app should have a backend side to return the data. This backend could be an API using **Python** or JavaScript with the framework you prefer, or something similar that emulates an API behavior.

### Appendix: Data details
The dataset is the file coupons.json which contains coupon data and discounts. Each coupon has the following fields:
* country_code: country code, always ‘us’
* coupon_id: unique coupon identifier
* coupon_webshop_name: coupon retailer name
* description: coupon description
* first_seen: first date coupon was seen
* last_seen: last date coupon was seen
* promotion_type: promotion type, could be **percent-off, buy-one-get-one, dollar-off, free-gift, free-shipping**
* title: coupon title
* value: numeric value, for **percent-off** coupons is % discount. For **dollar-of**, is discount in dollars $
* webshop_id: retailer code


### Points to appreciate
* Structure and code readability
* Components and split responsibility
* Good usage of the frameworks chosen
* Maintainability
* Data loading and handling
* RESTFull principes


