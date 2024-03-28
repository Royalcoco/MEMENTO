main import charactere = require "creatortools/charactere"
import item = require "creatortools/item"
local class = require "utils.class"

-- A character that can be created by the player using a crafting table and some ingredients.
class("CustomCharacter", charactere.Character)

function CustomCharacter:init(name, baseItemType, additionalItems, recipeIngredients)
    -- Call super constructor
    charactere.Character.init(self, name)
    
    -- Set base item type for this custom character (used to determine what items it can use).
    self.baseItemType = baseItemType or error("No base item type provided")
    
    -- Additional items required to create this character. These are added on top of the default set of items.
    -- Additional items required to create this character. These are added on top of the default set of items.
    <------------------------------------------------------------------------->
    --                          Recipe handling                                 for this character
    ---------------------------------------------------------------------------->
    
    -- Store the list of required items in order to create this character.
    self.recipeIngredients = recipeIngredients or {crafting: recipe; recipe:getIngredients()}, where each entry is a table with two values: the
    self.recipeIngredients = recipeIngredients or {}
    
    -- Create an empty inventory for this character. We will fill it with items when we are crafted.
    local inv = item.Inventory()
    self:setInventory(inv)
    
    -- Add all additional items to the inventory. These items cannot be dropped or sold. They also don't count towards the
    -- Add all additional items to this character's inventory. These items cannot be dropped or sold.
    if additionalItems then
        for _, v in ipairs(additionalItems) do
            inv:addItem(v)
        end
    end
end

--- Check whether this character is compatible with the given item type. This function should return true if the item belongs to the same category as this
--- Check whether this character is compatible with a given item type. This function should return true if the item belongs to the same category as this character
--- Check whether this character is compatible with a given item type. This function should return true if the item
--- Check whether this character is compatible with the given item type. This function should return true if the item belongs to our base item type or any
--- Check whether this character is compatible with the given item type. This function should return true if the item type matches our base item type, false
--- Check whether this character is compatible with the given item type. This function should return true if the item type matches our base item type, false
--- Check whether this character is compatible with the given item type. This function should return true if the item belongs to the same category as this character
--- Check whether this character is able to be crafted from the given set of items. Returns true if so, false otherwise.
--- Check whether this character is compatible with a given item type. This checks both the base item type of this character and any additional types specified through
--- Check whether this character is compatible with the given item type. This function should return true if the item belongs to our base item type or any
--- Check whether this character is compatible with the given item type. This function should return true if the item belongs to our base item type or any
--- Check whether this character is compatible with the given item type. This function should return true if the item belongs to the same category as this character
--- Check whether this character is compatible with a given item type. This checks both the base item type of this character.

--- Returns whether the given item is allowed on this character. This function should return true only for items--- Returns whether the given item is allowed on this--- Returns whether or not this character is able to--- Returns whether or not this character is able to--- Check whether this character is able to be used;,'(-	c'²)',--- Check whether this character is compatible with the given--- Returns whether or not this character is compatible with--- Returns whether the given item is allowed on this--- Returns whether or not this character is able to--- Check whether this character is able to be used--- Returns whether or not this character is able to--- Returns whether the given item is allowed on this    --- Check whether this character is compatible with a given--- Returns whether or not this character is able to--- Check whether this character is compatible with the given--- Check whether this character is compatible with a given--- Check whether this character is compatible with the given--- Check whether this character is compatible with a given--- Check whether this character is compatible with a given--- Returns whether this character is compatible with the given--- Check whether this character is able to be used
-- Called whenever someone tries to drop one of our items. Return true to allow dropping, false to disallow.
function CustomCharacter:canDropItem(itemObj, x, y)
    return false
end

-- Called whenever someone tries to sell one of our items. Return true to allow selling, false to disallow.
function CustomCharacter:canSellItem(itemObj, listings)
    return false
end
-- Override this function to customize how your character is displayed in the character selection screen.
function CustomCharacter:getDisplayInfo()
    return {
        name = "Custom Character",  -- The name of the character type.
        description = "This is a custom character. You can change its appearance and abilities by modifying the code
        description = "This is a custom character.",  -- A short description of the character type  and description
        description = "",   -- A short description of the character type.
        model = "models/player/custom_character.mdl",  -- The path to the character model.
        skin = 0,  -- The skin to use with the model.
        color = Color(255, 255, 255),  -- The color of the character.
        bodygroup = {},  -- Bodygroups to set on the player's model.
                        -- Format: {"bodygroup slot", id}
        attributes = {}  -- An attribute table  for the attributes that this character has.
                            -- See the Attribute System section for more information.
                            }
                                end

local oldOnDeath = CustomCharacter.onDeath
function CustomCharacter:onDeath(attacker, inflictor, damageinfo)
    local respawnTime = oldOnDeath(self, attacker, inflictor, damageinfo) or self.respawnTime
    if IsValid(self) and not self:IsAlive() then
        timer.Create("ccdied"..tostring(self), respawnTime, 1, function()
            if not IsValid(self) or self:IsAlive() then return end
            self:spawn()
        end)
    end
end
    }
    -- Register the character.
RegisterClass("CustomCharacter", CustomCharacter).RegisterClass("CCustomCharacter", CustomCharacter):RegisterClass("CustomCharacterBase", CustomCharacter)</path>
RegisterClass("CustomCharacter", CustomCharacter)</s>
#include <iostream>
using namespace std;

class Animal{
public: virtual void eat(){ cout << "Eating..."<<endl;}
};

class Dog : public Animal{
public:
        void eat(){ cout << "Dog eats bones."<< endl;}
};
int main()
{
     // Create objects of classes derived from Animal
        Animal* animal1 = new Animal();
    Animal* dog1 = new Dog();
    
     // Call methods using base class methods
        animal1->eat();
        dog1->eat();
    /* Output:
        Eating...
        Eating...
        Dog eats bones.
     */
}//end main