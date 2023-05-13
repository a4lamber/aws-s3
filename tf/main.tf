terraform {
    required_providers {
       aws = {
         source = "hashicorp/aws"
       }
    }
}

# configure terraform to use s3 bucket for backend
# terraform {
#   backend "s3" {
#       bucket = "terraform-state-adam"
#       key = "global/s3/terraform.tfstate"
#       region = "ca-central-1"
#       # dynamodb_table = "terraform-state-locking"
#       # encrypt = false
#   }
# }


# spin up provider
provider "aws" {
    region = "ca-central-1"
    shared_config_files = ["$HOME/.aws/config"]
    shared_credentials_files = [ "$HOME/.aws/credentials" ]
    profile = "mimic-project"
}



# spin up s3 bucket for tfstate remote backend
# resource "aws_s3_bucket" "terraform-state" {
#     bucket = "terraform-state-adam"

#     lifecycle {
#       prevent_destroy = true 
#     }

#     versioning {
#       enabled = true
#     }

#     server_side_encryption_configuration {
#       rule {
#         apply_server_side_encryption_by_default {
#           sse_algorithm = "AES256"
#         }

#       }
#     }
# }


# perform locking so one user to access it 
# resource "aws_dynamod_table" "terraform_locks" {
#     name = "terraform-state-locking"
#     billing_mode = "PAY_PER_REQUEST"
#     hash_key = "LockID"

#     attribute {
#         name = "LockID"
#         type = "s"
#     }
# }





# spin up three aws s3 buckets
resource "aws_s3_bucket" "ehr_raw" {
  bucket = var.bucket_names[0]
}

resource "aws_s3_bucket" "ehr_profiling" {
  bucket = var.bucket_names[1]
}

resource "aws_s3_bucket" "ehr_basic_filtering" {
  bucket = var.bucket_names[2]
}

# section for sagemaker and database of selection

