module WordCount (wordCount) where

import Data.Char

-- Split the string into a list of words.
-- For each word:
--  * count its occurances in the list
--  * remove from the list and recurse.

wCount :: [String] -> [(String, Int)] -> [(String, Int)]
wCount (s:xs) c =
  (:)
    (s, length . filter ((==) s) $ s:xs)
    $ wCount (filter ((/=) s) xs) c
wCount [] c = c

-- Drop chars unless alpha, digit or "'"
clean :: String -> String
clean s = map toLower . map (\x -> if (isAlpha x || isDigit x || x == '\'') then x else ' ') $ s

-- Unwrap wrapping single quotes from around a word
wClean :: [String] -> [String]
wClean xs = map (\x -> if ('\'' == (head x) && '\'' == (last x)) then (tail . init $ x) else x) xs

wordCount :: String -> [(String, Int)]
wordCount xs = wCount (wClean . words . clean $ xs) []
