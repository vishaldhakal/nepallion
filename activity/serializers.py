from .models import Activity,ActivityTestimonialImage,ActivityPricing,ActivityBooking,ActivityEnquiry,ActivityCategory,ItineraryActivity,ActivityImage,Destination,ActivityRegion,ActivityFAQ,ActivityTestimonial, ActivityCheckout
from rest_framework import serializers

class ActivityEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityEnquiry
        fields = ('id',)
        depth = 1

class ActivityTestimonialImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityTestimonialImage
        fields = ('image',)
        depth = 1

class ActivityTestimonialSerializer(serializers.ModelSerializer):
    images = ActivityTestimonialImageSerializer(many=True)
    class Meta:
        model = ActivityTestimonial
        exclude = ('activity',)
        depth = 1

class ActivitySmallestSer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('activity_title','priceSale','slug',)
        depth = 1
        
class ActivityBooking2Serializer(serializers.ModelSerializer):
    activity = ActivitySmallestSer(read_only=True)
    class Meta:
        model = ActivityBooking
        fields = ('id','no_of_guests','booking_date','activity')
        depth = 1
class ActivityBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityBooking
        fields = ('id','no_of_guests','booking_date',)
        depth = 1
class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'
        depth = 2

class ActivityRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityRegion
        fields = '__all__'
        depth = 1

class ActivityRegionSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityRegion
        fields = ['id','title','slug','image']
        depth = 1

class ActivityRegionSlugSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityRegion
        fields = ('id','slug')
        depth = 1

class DestinationSerializerSmall(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ('name',)

class DestinationNameSlugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ('name', 'slug')

class ActivityCategory2Serializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityCategory
        fields = ('title','image','image_alt_description','subtitle','slug')
        depth = 2

class ActivityCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityCategory
        fields = '__all__'
        depth = 2

class ActivityCategorySlugSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityCategory
        fields = ('id','slug')

class ActivityImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityImage
        fields = '__all__'

class ActivityPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPricing
        fields = '__all__'

class ActivityFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityFAQ
        fields = '__all__'

class ItineraryActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItineraryActivity
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    itinerary = ItineraryActivitySerializer(many=True, read_only=True)
    gallery = ActivityImageSerializer(many=True,read_only=True)
    faqs = ActivityFAQSerializer(many=True,read_only=True)
    enquiries = ActivityEnquirySerializer(many=True,read_only=True)
    testimonials = ActivityTestimonialSerializer(many=True,read_only=True)
    prices = ActivityPricingSerializer(many=True,read_only=True)
    
    class Meta:
        model = Activity
        fields = '__all__'
        depth = 2

class ActivitySmallSerializer(serializers.ModelSerializer):
    destination = DestinationSerializerSmall()
    enquiries = ActivityEnquirySerializer(many=True,read_only=True)
    class Meta:
        model = Activity
        fields = ('id','slug', 'activity_title', 'activity_category','enquiries','location','duration','price','coverImg','ratings','popular','best_selling','destination','activity_region','priceSale','youtube_link', 'trip_grade', 'max_group_size', 'trip_duration', 'group_size', 'trip_type', 'max_height')
        depth = 1

class DestinationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ('name', 'slug', 'thumnail_image')

class ActivityRegionInDestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityRegion
        fields = ('id', 'title', 'meta_title', 'meta_description', 'content', 'slug', 'image', 'image_alt_description', 'activity_category')
        depth = 1

class ActivityInDestinationSerializer(serializers.ModelSerializer):
    destination = DestinationSerializerSmall()
    activity_region = ActivityRegionInDestinationSerializer()
    
    class Meta:
        model = Activity
        fields = ('id', 'slug', 'activity_title', 'enquiries', 'location', 'duration', 'price', 
                 'coverImg', 'ratings', 'popular', 'best_selling', 'destination', 'activity_region', 
                 'priceSale', 'youtube_link', 'trip_grade', 'max_group_size', 'trip_duration', 
                 'group_size', 'trip_type', 'max_height')

class DestinationDetailSerializer(serializers.ModelSerializer):
    activities = ActivityInDestinationSerializer(many=True, read_only=True, source='activity_set')
    
    class Meta:
        model = Destination
        fields = '__all__'

class ActivitySmallestSerializer(serializers.ModelSerializer):
    destination = DestinationSerializerSmall()
    activity_category = ActivityCategorySerializer(many=True, read_only=True)
    activity_region = ActivityRegionSerializer(read_only=True)
    
    class Meta:
        model = Activity
        fields = ('id', 'slug', 'activity_title', 'destination', 'duration', 'price', 
                 'priceSale', 'trip_grade', 'max_group_size', 'best_time', 'activity_category',
                 'activity_region', 'coverImg')
        depth = 1

class ActivitySlugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id','slug')

class ActivityCategoryDetailSerializer(serializers.ModelSerializer):
    destination = DestinationSerializerSmall()
    activity_region = ActivityRegionSerializer()
    
    class Meta:
        model = Activity
        fields = [
            'id', 'slug', 'activity_title', 'enquiries', 'location', 
            'duration', 'price', 'coverImg', 'ratings', 'popular', 
            'best_selling', 'destination', 'activity_region', 'priceSale',
            'youtube_link', 'trip_grade', 'max_group_size', 'trip_duration',
            'group_size', 'trip_type', 'max_height'
        ]

class ActivityCheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityCheckout
        fields = [
            'id',
            'activity',
            'full_name',
            'email',
            'phone',
            'country',
            'total_travelers',
            'departure_date',
            'status',
            'created_at'
        ]
        read_only_fields = ['status', 'created_at']