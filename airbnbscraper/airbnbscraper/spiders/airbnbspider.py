import scrapy
import json
import re

class AirbnbspiderSpider(scrapy.Spider):
    name = "airbnbspider"
    
    # Define the parameters for the Airbnb search
    location = 'Calgary'
    location = location.replace(' ', '--')
    num_adult = 2
    num_child = 1
    num_pet = 1
    checkin = '2024-09-05'
    checkout = '2024-09-08'
    
    # Construct the base URL for the request
    base_url = f'https://www.airbnb.co.uk/s/{location}/homes?checkin={checkin}&checkout={checkout}&adults={num_adult}&children={num_child}&pets={num_pet}'

    def start_requests(self):
        # Start the request to the constructed URL
        yield scrapy.Request(url=self.base_url, callback=self.parse)

    def parse(self, response):
        # Extract the JSON data from the script tag
        data = response.xpath("//script[@id='data-deferred-state-0']/text()").get()
        jsdata = json.loads(data)

        # Target the specific results from the JSON data
        target_result = jsdata['niobeMinimalClientData'][0][1]['data']['presentation']['staysSearch']['results']['searchResults']

        for result in target_result:
            # Extract the required data, handling missing keys gracefully
            full_url = f'https://www.airbnb.co.uk/rooms/{result["listing"]["id"]}?adults={self.num_adult}&children={self.num_child}&pets={self.num_pet}&search_mode=regular_search&check_in={self.checkin}&check_out={self.checkout}'
            avg_rating = result['listing'].get('avgRatingA11yLabel', 'No rating available')
            room_id = result['listing']['id']
            title = result['listing']['name'] + ' ' + result['listing']['title']
            price_per_night = result['pricingQuote']['structuredStayDisplayPrice']['primaryLine'].get('accessibilityLabel', 'Price not available')
            total_price = result['pricingQuote']['structuredStayDisplayPrice']['secondaryLine'].get('accessibilityLabel', 'Total price not available')
            coordinates = f"latitude: {result['listing']['coordinate']['latitude']} longitude: {result['listing']['coordinate']['longitude']}"
            
            # Extract images if the 'contextualPictures' key exists
            images = [res['picture'] for res in result['listing'].get('contextualPictures', [])]
            
            # Extract options if they exist
            options_field = json.dumps(result['listing'].get('contextualPictures', []))
            options = re.findall(r'"messages":\s*\[(.*?)\]', options_field)

            # Yield the extracted data
            yield {
                'full_url': full_url,
                'avg rating': avg_rating,
                'room id': room_id,
                'title': title,
                'price per night': price_per_night,
                'total price': total_price,
                'coordinates': coordinates,
                'images': images,
                'options': options,
            }

         
        next_page =jsdata['niobeMinimalClientData'][0][1]['data']['presentation']['staysSearch']['results']['paginationInfo']['nextPageCursor'] 
        
        if next_page:
             next_url = self.base_url + f'&pagination_search=true&cursor={next_page}' 
             yield scrapy.Request(next_url, callback = self.parse)
             
             