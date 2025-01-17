# ttdrone_controller
Simple tutorial that shows how to use PyGame to create a controller for DJI's educational Tello Talent drone.

The Tello Talent comes with a Python module called `djitellopy` that communicates with the drone's UDP network interface. The drone understands commands like `move_forward(42)` and flies forward 42 cm. Of course the visual positioning system has issues, so even over the best of flying surfaces the drone is likely to respond to such a command by flying somewhere between 20 cm and 60 cm. These movement commands can be helpful to automate the drones movement through some programmed courses, but they would be horrible for a pilot's interface. Thankfully, DJI created another function to control the drone's flight in real-time: `send_rc_control(velocity_x, velocity_y, velocity_x, rotation)`. This project teaches how to use Pygame to setup a first-person controller using the drone's camera and the `send_rc_control` function.

Pygame is a common game engine with many features. It handles keyboard and mouse input well, has many built-in graphics options (blitting), and even allows you to add sound effects. This set of tutorials demonstrates the basic Pygame features that would be useful for a Tello Talent drone controller. The code is basic and expects users to expand upon it. Notably missing features are Pygame's surface transparency, sprite groups, and sprite collision detection. Although these feature are great for video games, they don't really apply to this flight controller.

I didn't have a drone on hand when I wrote the code, so I had to substitute my webcam for the drone's video feed. Of course, this also means that the controller keys don't make a real drone do anything. But all of the necessary drone commands are included in the comments. And towards the end, I show the necessary steps to switch from a webcam to the drone's video feed. For anyone with a little bit of Tello Talent programming experience, the final adjustments should be fairly straightforward.

Best wishes and happy flying!
Prof Tallman
