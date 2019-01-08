import os
import stripe

stripe_keys = {
  'secret_key': os.environ.get('SECRET_KEY'),
  'publishable_key': os.environ.get('PUBLISHABLE_KEY')
}

stripe.api_key = stripe_keys['secret_key']
