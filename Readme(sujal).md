# GymSync Website Documentation

## Project Overview
GymSync is a fitness-focused web application designed to attract gym enthusiasts ("gym freaks") by providing tools to create routines, add exercises, and stay updated with fitness news. The website features a consistent red (#dc3545) and gold (#DAA520) color scheme, with gray (#6c757d) for secondary elements, ensuring a professional and motivational aesthetic. The project includes multiple pages, each serving a specific purpose, with a static design (no JavaScript) to focus on layout and styling.

The website was developed iteratively based on user requirements, starting with a trainer dashboard (`index.html`), followed by specialized pages for creating routines (`new-routine.html`), adding exercises (`add-exercise.html`), a news page (`news.html`), and a creative homepage (`home.html`). The design ensures consistency across pages while incorporating vector images and a footer for enhanced usability.

## File Structure
The project consists of HTML and CSS files, organized as follows:

### HTML Files:
- **`index.html`**: The original trainer dashboard (static, no JavaScript) for managing users, routines, and time tracking.
- **`new-routine.html`**: A page for creating new routines, with a form for entering a routine name.
- **`add-exercise.html`**: A page for adding exercises to a category (e.g., "Chest"), with fields for name, description, sets, reps, and weight.
- **`news.html`**: A news page for author Suzanne Collins, featuring book announcements and reviews.
- **`home.html`**: The homepage, designed to attract gym enthusiasts with motivational content, featured workouts, and trainer highlights.

### CSS Files:
- **`styles.css`**: Styles for `index.html`, defining the overall theme (red and gold).
- **`new-routine.css`**: Styles for `new-routine.html`, matching the theme.
- **`add-exercise.css`**: Styles for `add-exercise.html`, consistent with the theme.
- **`news.css`**: Styles for `news.html`, adapted for a news layout.
- **`home.css`**: Styles for `home.html`, tailored for a gym-focused homepage.

**Note:** No external images or JavaScript files are used. Vector images (SVGs) are embedded inline in the HTML.

## Pages and Features

### 1. Trainer Dashboard (`index.html` and `styles.css`)
**Purpose:** A static dashboard for trainers to manage users, create routines, and track time.  
**Features:**
- Sidebar with buttons ("Manage Users", "Create Routine", "Track Time") stacked vertically to avoid overlap.
- Sections for user management, routine creation, and time tracking (hidden by default due to no JavaScript).
- Form for adding new users and routines (non-functional without JavaScript).

**Styling:**
- Sidebar uses `display: flex; flex-direction: column` with `gap: 20px` for spacing.
- Red (#dc3545) buttons turn gold (#DAA520) on hover.
- Sections have a white background with a gold top border.

### 2. Create Routine Page (`new-routine.html` and `new-routine.css`)
**Purpose:** A page for trainers to create new routines.  
**Features:**
- Form with a "Name" field, "Create Routine" (red) button, and "Cancel" (gray) button.
- Navigation with the gym name "GymSync" and links to other pages.

**Styling:**
- Input fields have a black border (`border: 1px solid #333`) with no border radius.
- Buttons are side by side using `display: flex` on `.button-group`.

### 3. Add Exercise Page (`add-exercise.html` and `add-exercise.css`)
**Purpose:** A page for trainers to add exercises to a category (e.g., "Chest").  
**Features:**
- Form with fields for "Name", "Description", "Sets", "Reps", and "Weight".
- "Add Exercise" (red) and "Cancel" (gray) buttons.
- Navigation with the gym name "GymSync".

**Styling:**
- Consistent with `new-routine.html`, with taller input fields (`height: 40px`).
- Form layout is vertical with clear labels.

### 4. Homepage (`home.html` and `home.css`)
**Purpose:** A creative homepage to attract gym enthusiasts.  
**Features:**
- Header: Displays the gym name "GymSync" and a navigation bar with links to "Home", "Create Routine", "Add Exercise", and "News".
- Hero Section: Motivational heading, tagline, "Join Now" button, and a vector image (dumbbell).
- Featured Workouts: Three workout cards (Powerlifting, HIIT, Bodyweight) with vector images.
- Elite Trainers: Three trainer cards with vector images.
- Call to Action: Encourages users to join with a "Get Started" button.
- Footer: Contact information and vertical navigation links.

**Styling:**
- Hero section has a large red heading and a prominent button.
- Workout and trainer cards use a grid layout with red borders that turn gold on hover.
- Footer has a red background with gold accents and a vertical nav.

## Vector Images (SVGs)
The homepage uses inline SVG vector images to replace raster images, maintaining the red (#dc3545) and gold (#DAA520) theme. Below are the SVG codes for each vector:

### 1. Hero Section Vector (Dumbbell)

<svg class="hero-image" width="500" height="500" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
    <circle cx="100" cy="100" r="80" fill="#dc3545" opacity="0.1"/>
    <path d="M60 140 L80 140 L80 60 L120 60 L120 140 L140 140 L140 40 L60 40 Z" fill="#dc3545"/>
    <circle cx="100" cy="100" r="10" fill="#DAA520"/>
</svg>


### 2. Powerlifting Workout Vector (Barbell with Weights)
<svg width="500" height="500" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <rect x="20" y="60" width="60" height="10" fill="#dc3545"/>
    <circle cx="20" cy="65" r="15" fill="#DAA520"/>
    <circle cx="80" cy="65" r="15" fill="#DAA520"/>
</svg>

### 3. HIIT Cardio Vector (Flame Icon)
<svg width="500" height="500" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <path d="M50 20 L70 40 L50 60 L30 40 Z" fill="#dc3545"/>
    <path d="M50 40 L60 50 L50 60 L40 50 Z" fill="#DAA520"/>
</svg>

### 4. Bodyweight Challenge Vector (Push-Up Stick Figure)
<svg width="500" height="500" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <circle cx="50" cy="30" r="15" fill="#dc3545"/>
    <path d="M50 45 L50 80 M30 60 L70 60" stroke="#DAA520" stroke-width="5" fill="none"/>
</svg>

### 5. Trainer Vector (Trainer Silhouette)
<svg width="500" height="500" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <circle cx="50" cy="30" r="15" fill="#dc3545"/>
    <path d="M50 45 L50 80 M30 60 L70 60 M30 50 L40 70 M60 70 L70 50" stroke="#DAA520" stroke-width="5" fill="none"/>
</svg>


## Styling Details
### Color Scheme:

- Primary: Red (#dc3545) for headers, buttons, and main headings.
- Secondary: Gold (#DAA520) for hover effects, subheadings, and accents.
- Tertiary: Gray (#6c757d) for secondary buttons (e.g., "Cancel").

### Typography:
Font: Arial, sans-serif for consistency and readability.

### Hierarchy: 

- h1 (2.5rem)
- h2 (1.8rem)
- h3 (1.2rem)
- Body text (1rem)

### Layout:
Containers use max-width: 1200px for a responsive design.

Sections have a white background, gold top border, and subtle shadow.

Grids (e.g., workout and trainer cards) use display: grid with repeat(3, 1fr), stacking on mobile.

## Responsive Design:
Media queries (@media (max-width: 768px)) stack grids and reduce padding/font sizes for smaller screens.

 ## Mock Ups 
So Tried to use Other languages like java with the html and css with Python but could not run in my laptop. So droppped the idea and stuck to front end and let armando do the backend with python and django treid to apply the java but time was limited.

## Mock up of the java 
![alt text](image.png)

### The Code Snippets
1. 
![alt text](image-1.png)
2. 
![alt text](image-2.png)
3. 
 ![alt text](image-3.png)
4. 
 ![alt text](image-4.png)
5. 
![alt text](image-5.png)
- So all of the above cose and mock up are animated and worked for the code but as we did not have any time left due to communication issues and pilling up our work we did not apply all of the requiremnets but at the end all of us communicated in the left two weeks to present a usable and running website you can check our progress in the issues that we created in github as a means of showing you that we have given our all. I dont know how many hours we gave but we have fulfilled the required hours to give to the project. Thank you!

## Conclusion 
The GymSync website project successfully delivers a cohesive and visually appealing platform for gym enthusiasts. The consistent red-and-gold theme creates a professional and motivational aesthetic, while the static design ensures a clean layout without the complexity of JavaScript. Each page serves a distinct purpose: the trainer dashboard (index.html) provides a foundation for user and routine management, new-routine.html and add-exercise.html offer tools for creating fitness content and home.html attracts users with a dynamic and engaging design.

The use of inline SVG vector images enhances the homepage's appeal, providing lightweight and scalable visuals that align with the gym theme. The addition of a footer with contact information and vertical navigation improves usability, ensuring users can easily navigate the site. The project is fully responsive, making it accessible on both desktop and mobile devices.

Future enhancements could include adding JavaScript for interactivity (e.g., form submissions, dynamic content updates), integrating a backend for data storage, or incorporating real gym images for a more realistic look. Overall, GymSync is a solid foundation for a fitness platform, ready to inspire and support gym enthusiasts in their fitness journey.

---
## Note:
Also There were not much to take from the web or any bibliography but i did Learn to create the Vector images from youtube and W3 schools as i didnot want to add a photo to a Webapp.
