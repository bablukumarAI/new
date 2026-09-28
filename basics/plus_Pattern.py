n = int(input("Enter the no's of lines :"))

mid = n // 2
for i in range(n):
    for j in range(n):
        if i == mid or j == mid:
            print("*", end = "")
        else:
            print(" ", end = "")
    print()


# #include<iostream>
# using namespace std;
# int main(){
#     int n;
#     cout<<"Enter a odd number :";
#     cin>>n;
#     for(int i=1;i<=n;i++){
#         for(int j=1;j<=n;j++){
#             if(i==n/2+1 || j==n/2+1){
#                 cout<<"*";
#             }
#             else cout<<" ";
#         }
#         cout<<endl;
#     }
#     return 0;
# }