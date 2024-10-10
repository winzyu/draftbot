# Install and load the necessary packages if not already installed
# install.packages("dplyr")
library(dplyr)

# Read the CSV file into a data frame
df <- read.csv("bs_pins_by_brawler.csv", stringsAsFactors = FALSE)

# Filter out rows where 'brawler_link' contains "category"
# and 'pin_img-src' contains "data:image/gif" or "NA"
cleaned_df <- df %>% 
  filter(!grepl("category", brawler_link, ignore.case = TRUE),
         !grepl("data:image/gif", `pin_img-src`, ignore.case = TRUE),
         !is.na(`pin_img-src`))

# Save the cleaned data to a new CSV file
write.csv(cleaned_df, "cleaned_bs_pins_by_brawler.csv", row.names = FALSE)
