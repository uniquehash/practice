import Graphics.Element exposing (..)
import Mouse 
import Debug

main : Signal Element 
main = 
  Signal.map show (Signal.map (Debug.watch "mouse") Mouse.position)




