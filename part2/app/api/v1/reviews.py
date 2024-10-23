from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('reviews', description='Review operations')


review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

facade = HBnBFacade()

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        try:
            review_data = api.payload
            creating_review = facade.create_review(review_data)
            if creating_review:
                return {'review_id': creating_review.id, 'reviewdata': review_data}, 201
            else:
                return {'message': 'Invalid input data'}, 400
        except Exception as e:
            return {'message': str(e)}, 400
    

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        get_all_reviews = facade.get_all_reviews()
        review_list = []
        for review in get_all_reviews:
            review_list.append({
                'review_id': review.id,
                'user_id': review.user_id,
                'place_id': review.place_id,
                'comment': review.comment,
                'rating': review.rating,
            })
        return ({'get_all_reviews' : review_list}), 200
        

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        
        review_data = {
            'review_id': review.id,
            'user_id': review.user_id,
            'place_id': review.place_id,
            'comment': review.comment,
            'rating': review.rating,
        }
        return {'review_data':'Review details retrieved successfully'}, 200
    

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review's information"""
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        facade.update_review(review_id)

        return {'message': 'Review updated successfully'}, 200


    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        review = facade.get_review(review_id)

        if not review:
            return {'error': 'Review not found'}, 404
        facade.delete_review(review_id)
        
        return {'message': 'Review deleted successfully'}, 200


@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        reviews = facade.get_reviews_by_place(place_id)
        if reviews is None:
            return {'error': 'Place not found'}, 404
        
        reviews_list = [review.to_dict() for review in reviews]
        return {'reviews': reviews_list}, 200