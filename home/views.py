from django.shortcuts import render,HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FAQ,FAQCategory,LegalDocument,FeaturedTour,TeamMember,Testimonial,SiteConfiguration,Affiliations,Partners,DestinationNavDropdown, OtherActivitiesNavDropdown, InnerDropdown, ClimbingNavDropdown, TreekingNavDropdown,NewsletterSubscription
from .serializers import FAQSerializer,LegalDocumentSerializer,FeaturedTourSerializer,FAQCategorySerializer,TeamMemberSlugSerializer,TestimonialSerializer,TeamMemberSerializer,AffiliationsSerializer,PartnersSerializer,SiteConfigurationSerializer,DestinationNavDropdownSerializer, OtherActivitiesNavDropdownSerializer, ClimbingNavDropdownSerializer, TreekingNavDropdownSerializer
from blog.models import Post
from blog.serializers import PostSmallSerializer
from activity.models import ActivityCategory,Activity,ActivityEnquiry,ActivityBooking
from activity.serializers import ActivityCategorySerializer,ActivitySmallSerializer,ActivityCategory2Serializer,ActivitySmallestSerializer,ActivityBooking2Serializer
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime
from datetime import date
import re

@api_view(["POST"])
def ContactFormSubmission(request):
    if request.method == "POST":
        subject = "Contact Form Submission"
        email = "Nepal Lion Trekking <info@nepallion.com>"
        headers = {'Reply-To': request.POST["email"]}
        contex = {
            "name": request.POST["name"],
            "email": request.POST["email"],
            "phone": request.POST["phone"],
            "message": request.POST["message"]
        }
        html_content = render_to_string("contactForm.html", contex)
        text_content = strip_tags(html_content)

        msg = EmailMultiAlternatives(subject, "You have been sent a Contact Form Submission. Unable to Receive !", email, ["nepallions790@gmail.com"], headers=headers)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return HttpResponse("Sucess")
    else:
        return HttpResponse("Not post req")

@api_view(["POST"])
def InquirySubmission(request):
    if request.method == "POST":
        subject = "Enquiry About Activity"
        email = "Yeti Hikes <info@nepallions.com>"
        headers = {'Reply-To': request.POST["email"]}

        actt = Activity.objects.get(slug=request.POST["slug"])
        if request.POST["phone"]:
            chh = request.POST["phone"]
        else:
            chh = "No Number"

        neww = ActivityEnquiry.objects.create(activity=actt,name=request.POST["name"],email=request.POST["email"],message=request.POST["message"],phone=chh)
        neww.save()

        contex = {
            "name": request.POST["name"],
            "email": request.POST["email"],
            "phone": request.POST["phone"],
            "message": request.POST["message"],
            "activity": actt.activity_title,
            "slug": request.POST["slug"]
        }

        html_content = render_to_string("contactForm2.html", contex)
        text_content = strip_tags(html_content)

        msg = EmailMultiAlternatives(subject, "You have been sent a Contact Form Submission. Unable to Receive !", email, ["nepallions790@gmail.com"], headers=headers)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return HttpResponse("Sucess")
    else:
        return HttpResponse("Not post req")

@api_view(["POST"])
def PlanTripSubmit(request):
    if request.method == "POST":
        subject = "Customized Trip Enquiry"
        email = "Yeti Hikes <info@nepallions.com>"
        headers = {'Reply-To': request.POST["email"]}

        actt = Activity.objects.get(slug=request.POST["slug"])

        contex = {
            "name": request.POST["name"],
            "email": request.POST["email"],
            "phone": request.POST["phone"],
            "message": request.POST["message"],
            "noofpeople": request.POST["no_of_people"],
            "noofdays": request.POST["no_of_days"],
            "arrival": request.POST["arrival"],
            "departure": request.POST["departure"],
            "budget_from": request.POST["budget_from"],
            "budget_to": request.POST["budget_to"],
            "activity": actt.activity_title,
            "slug": request.POST["slug"]
        }

        html_content = render_to_string("ContactForm4.html", contex)
        text_content = strip_tags(html_content)

        msg = EmailMultiAlternatives(subject, "You have been sent a Contact Form Submission. Unable to Receive !", email, ["nepallions790@gmail.com"], headers=headers)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return HttpResponse("Sucess")
    else:
        return HttpResponse("Not post req")

@api_view(["POST"])
def BookingSubmission(request):
    if request.method == "POST":
        try:
            subject = "Booking of Activity"
            email = "Yeti Hikes <info@nepallions.com>"
            headers = {'Reply-To': request.POST["email"]}

            name = request.POST.get("name", "")
            address = request.POST.get("address", "")
            emaill = request.POST.get("email", "")
            phone = request.POST.get("phone", "")
            message = request.POST.get("message", "")

            try:
                no_of_guests = int(request.POST.get("no_of_guests", "0"))
            except ValueError:
                no_of_guests_str = request.POST.get("no_of_guests", "1")
                match = re.search(r'(\d+)', no_of_guests_str)
                no_of_guests = int(match.group(1)) if match else 1

            total_price = float(request.POST.get("total_price", "0.0"))
            booking_date_str = request.POST.get("booking_date", "")
            arrival_date_str = request.POST.get("arrival_date", "")
            private_booking = request.POST.get("private_booking", "False")
            departure_date_str = request.POST.get("departure_date", "")
            group_size = request.POST.get("group_size", "")
            group_price_id = request.POST.get("group_price_id", "")

            booking_date = datetime.strptime(booking_date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
            arrival_date = datetime.strptime(arrival_date_str, '%Y-%m-%dT%H:%M:%S.%fZ') if arrival_date_str else None
            departure_date = datetime.strptime(departure_date_str, '%Y-%m-%dT%H:%M:%S.%fZ') if departure_date_str else None

            emergency_contact_name = request.POST.get("emergency_contact_name", "")
            emergency_address = request.POST.get("emergency_address", "")
            emergency_phone = request.POST.get("emergency_phone", "")
            emergency_email = request.POST.get("emergency_email", "")
            emergency_relationship = request.POST.get("emergency_relationship", "")

            act = Activity.objects.get(slug=request.POST["slug"])

            contex = {
                "name": request.POST["name"],
                "email": request.POST["email"],
                "phone": request.POST["phone"],
                "message": request.POST["message"],
                "total_price": request.POST["total_price"],
                "no_of_guests": no_of_guests,
                "booking_date": request.POST["booking_date"],
                "activity": act.activity_title,
                "slug": request.POST["slug"],
                "group_size": group_size
            }

            html_content = render_to_string("contactForm3.html", contex)
            text_content = strip_tags(html_content)

            msg = EmailMultiAlternatives(subject, "You have been sent a Contact Form Submission. Unable to Receive !", email, ["nepallions790@gmail.com"], headers=headers)
            msg.attach_alternative(html_content, "text/html")
            msg.send()


            new_booking = ActivityBooking.objects.create(
                activity=act,
                name=name,
                address=address,
                email=emaill,
                no_of_guests=no_of_guests,
                total_price=total_price,
                booking_date=booking_date
            )
            if "private_booking" in request.POST:
                if private_booking == "True":
                    new_booking.is_private = True
                else:
                    new_booking.is_private = False
            if "phone" in request.POST:
                new_booking.phone = phone
            if "message" in request.POST:
                new_booking.message = message
            if "arrival_date" in request.POST:
                new_booking.arrival_date = arrival_date
            if "departure_date" in request.POST:
                new_booking.departure_date = departure_date
            if "emergency_contact_name" in request.POST:
                new_booking.emergency_contact_name = emergency_contact_name
            if "emergency_address" in request.POST:
                new_booking.emergency_address = emergency_address
            if "emergency_phone" in request.POST:
                new_booking.emergency_phone = emergency_phone
            if "emergency_email" in request.POST:
                new_booking.emergency_email = emergency_email
            if "emergency_relationship" in request.POST:
                new_booking.emergency_relationship = emergency_relationship
            if "group_size" in request.POST:
                new_booking.group_size = group_size
            if "group_price_id" in request.POST:
                new_booking.group_price_id = group_price_id
            new_booking.save()

            return HttpResponse("Success")
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}", status=400)
    else:
        return HttpResponse("Not post req")

@api_view(['POST'])
def Newsletter(request):
    emaill = request.POST.get("email")
    nsss = NewsletterSubscription.objects.create(email=emaill)
    nsss.save()
    """ subject = "Newsletter Subscribed" """

    """ body = f"Newsletter Subscribed by {emaill}\n" """

    """ send_mail(subject, body, "info@nepallions.com",  [emaill,"info@nepallions.com"], fail_silently=False) """
    return Response({'success': "Subscribed Sucessfully"},status=status.HTTP_200_OK)

@api_view(['GET'])
def legaldocuments(request):
    legal_documents = LegalDocument.objects.all()
    legal_documents_serializer = LegalDocumentSerializer(legal_documents, many=True)
    return Response({'legal_documents': legal_documents_serializer.data})

@api_view(['GET'])
def faq_list(request):
    faqs = FAQ.objects.all()
    serializer = FAQSerializer(faqs, many=True)
    
    faq_cats = FAQCategory.objects.all()
    serializer_cat = FAQCategorySerializer(faq_cats, many=True)
    
    return Response({'faqs': serializer.data,"faq_categories":serializer_cat.data})


@api_view(['GET'])
def navbar(request):
    if request.method == 'GET':
        destination_nav = DestinationNavDropdown.objects.get()
        destination_nav_serializer = DestinationNavDropdownSerializer(destination_nav)

        other_nav = OtherActivitiesNavDropdown.objects.get()
        other_nav_serializer = OtherActivitiesNavDropdownSerializer(other_nav)
        
        acy = ActivityCategory.objects.get(title="Peak Climbing")
        climb_nav = Activity.objects.filter(activity_category=acy)
        climb_nav_serializer = ActivitySmallSerializer(climb_nav,many=True)

        trek_nav = TreekingNavDropdown.objects.get()
        trek_nav_serializer = TreekingNavDropdownSerializer(trek_nav)
        
        return Response({
          "destination_nav":destination_nav_serializer.data,
          "other_activities_nav":other_nav_serializer.data,
          "climbing_nav":climb_nav_serializer.data,
          "trekking_nav":trek_nav_serializer.data,
        })


@api_view(['GET'])
def landing_page(request):
    if request.method == 'GET':
        today = date.today()

        teammembers = TeamMember.objects.all()
        teammembers_serializer = TeamMemberSerializer(teammembers,many=True)

        testimonial = Testimonial.objects.all()
        testimonial_serializer = TestimonialSerializer(testimonial,many=True)
        
        hero_content = SiteConfiguration.objects.get()
        hero_content_serializer = SiteConfigurationSerializer(hero_content)

        posts = Post.objects.all()[:5]
        posts_serializer = PostSmallSerializer(posts,many=True)
        
        bookings = ActivityBooking.objects.filter(booking_date__gte=today).order_by('-booking_date')[:10]
        bookings_serializer = ActivityBooking2Serializer(bookings,many=True)

        try:
            activities = FeaturedTour.objects.get()
            featured_tours = Activity.objects.filter(id__in=activities.featured_tours.all())
            popular_tours = Activity.objects.filter(id__in=activities.popular_tours.all())
            best_selling_tours = Activity.objects.filter(id__in=activities.best_selling_tours.all())
            favourite_tours = Activity.objects.filter(id__in=activities.favourite_tours.all())
            banner_tour = activities.banner_tour.first()  # Get the first banner tour if exists
        except FeaturedTour.DoesNotExist:
            featured_tours = []
            popular_tours = []
            best_selling_tours = []
            favourite_tours = []
            banner_tour = None

        featured_serializer = ActivitySmallestSerializer(featured_tours, many=True)
        popular_serializer = ActivitySmallestSerializer(popular_tours, many=True)
        best_selling_serializer = ActivitySmallestSerializer(best_selling_tours, many=True)
        favourite_serializer = ActivitySmallestSerializer(favourite_tours, many=True)
        banner_serializer = ActivitySmallestSerializer(banner_tour) if banner_tour else None
        
        activity_category = ActivityCategory.objects.all()
        serializer_activity_category = ActivityCategory2Serializer(activity_category, many=True)
        
        affiliations = Affiliations.objects.all()
        serializer_affiliations = AffiliationsSerializer(affiliations, many=True)
        
        partners = Partners.objects.all()
        serializer_partners = PartnersSerializer(partners, many=True)
        
        return Response({
          "hero_content":hero_content_serializer.data,
          "recent_posts":posts_serializer.data,
          "featured_activities":featured_serializer.data,
          "popular_activities":popular_serializer.data,
          "best_selling_activities":best_selling_serializer.data,
          "favourite_activities":favourite_serializer.data,
          "banner_activity":banner_serializer.data if banner_serializer else {},
          "activity_categories":serializer_activity_category.data,
          "team_members":teammembers_serializer.data,
          "testimonials":testimonial_serializer.data,
          "affiliations":serializer_affiliations.data,
          "partners":serializer_partners.data,
          "bookings":bookings_serializer.data,
        })

@api_view(['GET'])
def all_bookings(request):
    if request.method == 'GET':
        bookings = ActivityBooking.objects.all().order_by('-booking_date')
        bookings_serializer = ActivityBooking2Serializer(bookings,many=True)
        
        return Response({
          "bookings":bookings_serializer.data,
        })


@api_view(['GET'])
def testimonials(request):
    if request.method == 'GET':
        testimonial = Testimonial.objects.all()
        testimonial_serializer = TestimonialSerializer(testimonial,many=True)
        
        return Response({
          "testimonials":testimonial_serializer.data,
        })

@api_view(['GET'])
def teams_id(request):
    if request.method == 'GET':
        teammembers = TeamMember.objects.all()
        teammembers_serializer = TeamMemberSlugSerializer(teammembers,many=True)
        
        return Response({
          "team_members":teammembers_serializer.data,
        })

@api_view(['GET'])
def teams(request):
    if request.method == 'GET':
        teammembers = TeamMember.objects.all()
        teammembers_serializer = TeamMemberSerializer(teammembers,many=True)
        
        return Response({
          "team_members":teammembers_serializer.data,
        })

@api_view(['GET'])
def teams_single(request,id):
    if request.method == 'GET':
        teammembers = TeamMember.objects.get(id=id)
        teammembers_serializer = TeamMemberSerializer(teammembers)
        
        return Response({
          "team_member":teammembers_serializer.data,
        })

@api_view(["GET"])
def slider_tours(request):
    try:
        featured_tour = FeaturedTour.objects.prefetch_related('slider_tours__prices').get()
        slider_tours = featured_tour.slider_tours.all()
        serializer = ActivitySmallSerializer(slider_tours, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    except FeaturedTour.DoesNotExist:
        return Response({"status": "error", "message": "No slider tours found"}, status=status.HTTP_404_NOT_FOUND)