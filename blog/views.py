from datetime import date

from django.shortcuts import render

# Create your views here.

all_posts = [
    {
        "slug":"Hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Yasin",
        "date": date(2024 ,3 ,8),
        "title" : "Mountain Hiking",
        "excerpt" : "Mountain hiking offers a thrilling escape into the rugged beauty of nature, where adventurers can challenge themselves against towering peaks and breathtaking landscapes. ",
        "content":""""
                Mountain hiking is a remarkable adventure that combines physical exertion with the splendor of nature. As you lace up your hiking boots and set out on the trail, you embark on a journey filled with excitement and discovery.

                The ascent begins gently, with each step bringing you closer to the towering peaks that loom overhead. The trail winds its way through lush forests, where sunlight filters through the canopy above, casting dappled shadows on the forest floor.

                As you gain elevation, the landscape changes dramatically. The trees thin out, giving way to alpine meadows dotted with colorful wildflowers. The air grows cooler and thinner, invigorating your senses and spurring you onward.

                With each switchback and scramble, you push yourself to new heights, fueled by the promise of the spectacular views that await at the summit. Finally, after hours of hiking, you reach the pinnacle of your journey, where the world stretches out before you in all its glory.

                From your vantage point high above the valley below, you can see for miles in every direction. Snow-capped peaks pierce the sky, while rivers wind their way through verdant valleys far below. The beauty of the natural world unfolds before you, a breathtaking panorama that defies description.

                But the true reward of mountain hiking isn't just the view from the top—it's the journey itself. It's the sense of accomplishment that comes from pushing your limits and conquering challenges along the way. It's the camaraderie shared with fellow hikers, as you swap stories and share snacks at rest stops along the trail.

                As the sun begins to dip below the horizon, casting a warm golden glow over the landscape, you begin your descent, your heart full of memories and your spirit rejuvenated by the beauty of the mountains. And as you make your way back to civilization, you carry with you a newfound appreciation for the majesty of the natural world and the joys of outdoor adventure.
                """,
    },
        {
        "slug": "Programming",
        "image": "coding.png",
        "author": "Yasin",
        "date": date(2024 ,3 ,8),
        "title" : "Programming",
        "excerpt" : "Programming is the art of instructing computers to perform tasks through the use of algorithms and code. It empowers individuals to create software solutions that automate processes, solve problems, and enhance efficiency.",
        "content":"""
                Programming is both a science and an art. It involves the systematic writing of instructions (code) that tell computers how to perform specific tasks. At its core, programming requires logical thinking and problem-solving skills.

                One of the fundamental concepts in programming is understanding algorithms, which are step-by-step procedures for solving problems. These algorithms are translated into code using programming languages such as Python, Java, C++, and many others.

                As programmers, we use various tools and technologies to write, debug, and maintain code. Integrated Development Environments (IDEs) provide a comprehensive environment for writing and testing code, while version control systems like Git help us manage changes and collaborate with other developers.

                The field of programming is vast and constantly evolving. From web development and mobile app development to data science and machine learning, there are numerous specialties and niches to explore. Each area comes with its own set of languages, frameworks, and best practices.

                Despite its complexities, programming offers immense opportunities for creativity and innovation. Whether you're building a simple website or developing complex algorithms for artificial intelligence, programming allows you to bring your ideas to life and make a meaningful impact in the digital world.
                """,
    },
{
    "slug": "Nature-is-best",
    "image": "woods.jpg",
    "author": "Yasin",
    "date": date(2024, 3, 8),
    "title": "Nature",
    "excerpt": "Nature's beauty is unparalleled, with its vast landscapes, diverse flora, and fauna. Exploring the great outdoors brings a sense of peace and wonder, immersing oneself in the serenity of forests, the majesty of mountains, and the tranquility of rivers.",
    "content": """
        Nature's beauty is truly awe-inspiring. As I ventured into the heart of the forest, I was immediately struck by the vibrant colors and soothing sounds surrounding me. Shafts of sunlight filtered through the dense canopy above, dappling the forest floor with patches of golden light.

        The air was alive with the chirping of birds and the rustling of leaves as squirrels scurried about their daily activities. I couldn't help but feel a profound sense of peace wash over me, as if nature itself was embracing me in its loving embrace.

        I followed a winding trail deeper into the woods, the earthy scent of moss and damp soil filling my nostrils. Every step brought me closer to the heart of nature, away from the hustle and bustle of the modern world.

        As I walked, I marveled at the intricate beauty of the flora and fauna around me. Delicate ferns unfurled their fronds in the dappled sunlight, while colorful wildflowers carpeted the forest floor in a riot of hues.

        Reaching a clearing, I was greeted by the sight of a crystal-clear stream meandering through the landscape. The water glistened in the sunlight, inviting me to dip my toes in its cool embrace. I sat by the stream for a while, listening to the gentle babbling of the water as it flowed over smooth stones.

        In that moment, surrounded by the beauty of nature, I felt truly alive. It was as if the worries and stresses of everyday life had melted away, leaving only a sense of peace and contentment in their wake.

        As the sun began to set, casting a warm golden glow over the landscape, I reluctantly bid farewell to the forest and made my way back to civilization. But even as I returned to the hustle and bustle of the modern world, I carried with me a newfound appreciation for the beauty and wonder of nature.
        """
}
]

def get_date(post):
    return post['date']



def starting_page(request):
    sorted_post = sorted(all_posts , key=get_date)
    latest_post = sorted_post[-3:]
    return render(request , "blog/index.html" , {
        "posts" : latest_post
    })


def posts(request):
    return render(request , "blog/all-posts.html" , {
        "all_posts": all_posts
    } )

def singel_detail(request , slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request , "blog/post-detail.html" , {
        "post" : identified_post
    } )