clear all
%close all
clc
coinc1= zeros(500);
count= 0;

% s300_s800 = xlsread('131_silicon_coincidences.xlsx','300800','B2:D64499');
% s300_s800(:,2) = s300_s800(:,2).*1000;
% s300_s800(:,3) = s300_s800(:,3).*1000;
% 
% s300_s900 = xlsread('131_silicon_coincidences.xlsx','300900','B2:D17447');
% s300_s900(:,2) = s300_s900(:,2).*1000;
% s300_s900(:,3) = s300_s900(:,3).*1000;
% 
% s400_s800 = xlsread('131_silicon_coincidences.xlsx','400800','B2:D17587');
% s400_s800(:,2) = s400_s800(:,2).*1000;
% s400_s800(:,3) = s400_s800(:,3).*1000;
% 
% % s300_s800b = xlsread('131_coincidences_book.xlsx','300800b','B1:D232579');
% % s300_s800b(:,2) = s300_s800b(:,2).*1000;
% % s300_s800b(:,3) = s300_s800b(:,3).*1000;
% 
% s400_s900 = xlsread('131_silicon_coincidences.xlsx','400900','B2:D64373');
% s400_s900(:,2) = s400_s900(:,2).*1000;
% s400_s900(:,3) = s400_s900(:,3).*1000;
% 
% % s400_s900b = xlsread('131_coincidences_book.xlsx','400900b','B1:D233097');
% % s400_s900b(:,2) = s400_s900b(:,2).*1000;
% % s400_s900b(:,3) = s400_s900b(:,3).*1000;

%A = cat(1,s300_s900,s400_s800,s300_s800,s400_s900);
load('sortedmat.mat');
[m,n] = size(sortedmat) 
%[m,n] = size(A)
%m = 100000;
eth = 40;
for i = 1:m 
    if (sortedmat(i,2) > eth)
    Y = ceil(normrnd(sortedmat(i,2),(0.17/2.35)*sortedmat(i,2)));
    %Y = ceil(A(i,3));
    X = ceil(normrnd(sortedmat(i,3),(0.17/2.35)*sortedmat(i,3)));
    %X = ceil(A(i,4));
    coinc1(X,Y) = coinc1(X,Y)+1;
    count = count +1; 
    %end
    %percentage_done = (i/m) *100
    end
end
figure(1)
h=surfc(coinc1);
set(h,'LineStyle','none')
set(gca, 'FontSize', 14)
colorbar
colormap jet
xlabel('Energy (kev), Silicon 1 + Silicon 2','Fontsize', 14);
ylabel('Energy (kev), CZT 1 + CZT 2','Fontsize', 14);
title('131mXe electron-photon Coincidence','FontSize', 14, 'fontweight','bold');
axis square
xlim([0 170]);
ylim([0 170]);
%zlim([0,1000000]);