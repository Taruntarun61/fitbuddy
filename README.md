**Set Up the Base HTML Structure**

- Developed index.html as the main entry point for user input.
- Structured the form to capture:
  - username, user_id, age, weight, goal, and intensity.
- Each field is properly labeled and grouped using semantic HTML.
- The design uses a gym-themed background image, Google Fonts (Roboto), and bold typography to create a clean, fitness-oriented interface.
- Navigation is kept minimal for focus, and user flow directs clearly from input to output.

**Design a Responsive Layout Using CSS**

- Embedded CSS styles were applied directly in each HTML file.
- Layouts use Flexbox to center content both vertically and horizontally.
- Media queries ensure mobile responsiveness.
- Buttons have consistent styling with hover effects.
- Input fields and result blocks have adequate padding, shadows, and rounded corners for modern aesthetics.
- Overall color scheme supports readability on a dark background.

**Create Separate Pages for Each Core Functionality**

Three Jinja2-powered HTML templates were created under /templates:

- index.html: A user input form with fields for fitness goal, intensity, and basic personal information.
- result.html: Displays the 7-day AI generated workout plan, a nutrition tip, and accepts user feedback.
- all_users.html: Admin panel to view and delete users and review both original and updated plans.

Templates are modular, and UI transitions smoothly between steps.

Forms are submitted to specific FastAPI endpoints via POST methods# fitbuddy
AI Fitness Plan Generator
