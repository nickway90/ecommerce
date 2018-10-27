import os
import stripe

stripe_keys = {
  'secret_key': os.environ.get('SECRET_KEY', 'sk_test_vh7QAMSOSJFhgi3mjdcZzBjT'),
  'publishable_key': os.environ.get('PUBLISHABLE_KEY', 'pk_test_JqaiFr4mZjXgiGRd4BvkpKgz')
}

stripe.api_key = stripe_keys['secret_key']
